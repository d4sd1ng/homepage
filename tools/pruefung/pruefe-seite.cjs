#!/usr/bin/env node
/*
 * Nurovelle - Pflichtpruefung einer Detailseite.
 *
 * Prueft eine umgestellte Seite gegen die Vorlage homepage/analyse.html,
 * gegen styleguide.md Abschnitt 21 und gegen die Quellseite, aus der die
 * Texte stammen. Liest nur, aendert nichts.
 *
 *   node tools/pruefung/pruefe-seite.cjs <seite.html> [quellseite.html]
 *
 * Beispiel:
 *   node tools/pruefung/pruefe-seite.cjs preview-detail_roadmap.html detail_roadmap.html
 *
 * Rueckgabewert 0, wenn jede Regel bestanden ist, sonst 1.
 */

const fs = require('fs');
const path = require('path');
const http = require('http');
const crypto = require('crypto');
const { chromium } = require('playwright');

const WURZEL = path.resolve(__dirname, '..', '..', 'homepage');
const VORLAGE = 'analyse.html';
const BREITEN = [390, 768, 1100, 1440, 1600, 1920, 2560];

// Verbindliche Werte, styleguide.md Abschnitt 21. Nur ab 901 px gueltig.
const SOLL = {
  inhalt: 1300,          // 21.0 Inhaltsbreite
  einzug: 32,            // 21.1 Mindesteinzug je Seite
  karte: 634,            // 21.1 Karte im Zweierraster
  listeneintrag: 622,    // 21.1 Eintrag in der num-list
  bild: 544,             // 21.2 Bild im media-split
  textspalte: 700,       // 21.2 Textspalte im media-split
  subline: 820,          // 21.1 Subline max-width
  sublineDefinition: 850, // Vorlage setzt in .definition-intro 850; 21.1 nennt 820
  faqKnopf: 640,         // 21.4 Breite je FAQ-Knopf
  iconRahmen: 54,        // 21.3 module-icon-frame
  icon: 41               // 21.3 module-icon
};

const BLOECKE = [
  ['Karten', '.analysis-intro-cards'],
  ['Fliesstext', '.section:not(#hero) .text'],
  ['media-split', '.media-split'],
  ['num-list', '.num-list'],
  ['chip-list', '.chip-list'],
  ['breites Feld', '#einsatzbereiche > .section-inner > .panel'],
  ['FAQ-Raster', '.faq-grid']
];

const ergebnisse = [];
function melde(regel, bestanden, text) {
  ergebnisse.push({ regel, bestanden, text });
}

const TYPEN = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp',
  '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.ico': 'image/x-icon' };

function server() {
  return new Promise(fertig => {
    const s = http.createServer((req, res) => {
      const p = path.join(WURZEL, decodeURIComponent(req.url.split('?')[0]));
      if (!p.startsWith(WURZEL) || !fs.existsSync(p) || fs.statSync(p).isDirectory()) {
        res.writeHead(404); return res.end();
      }
      res.writeHead(200, { 'Content-Type': TYPEN[path.extname(p).toLowerCase()] || 'application/octet-stream' });
      fs.createReadStream(p).pipe(res);
    });
    s.listen(0, '127.0.0.1', () => fertig({ s, port: s.address().port }));
  });
}

// ---------------------------------------------------------------- Textwerkzeug
function ohneRahmen(html) {
  return html
    .replace(/<header[\s\S]*?<\/header>/g, '')
    .replace(/<footer[\s\S]*?<\/footer>/g, '')
    .replace(/<(script|style|svg)\b[\s\S]*?<\/\1>/gi, ' ')
    .replace(/<!--[\s\S]*?-->/g, ' ');
}
function textstuecke(html) {
  return ohneRahmen(html).split(/<[^>]+>/)
    .map(t => t.replace(/&(amp|lt|gt|quot|#39|nbsp);/g, ' ').replace(/\s+/g, ' ').trim())
    .filter(t => t.length > 3);
}
function links(html) {
  const out = [];
  const re = /<a[^>]+href="([^"]+)"/g;
  let m; const k = ohneRahmen(html);
  while ((m = re.exec(k))) out.push(m[1]);
  return out;
}
function block(html, tag) {
  const m = html.match(new RegExp(`<${tag}[^>]*>[\\s\\S]*?<\\/${tag}>`));
  return m ? crypto.createHash('sha256').update(m[0]).digest('hex').slice(0, 12) : null;
}

(async () => {
  const datei = process.argv[2];
  const quelle = process.argv[3];
  if (!datei) {
    console.error('Aufruf: node tools/pruefung/pruefe-seite.cjs <seite.html> [quellseite.html]');
    process.exit(2);
  }
  for (const f of [datei, VORLAGE, quelle].filter(Boolean)) {
    if (!fs.existsSync(path.join(WURZEL, f))) {
      console.error(`Datei fehlt: homepage/${f}`); process.exit(2);
    }
  }

  const seite = fs.readFileSync(path.join(WURZEL, datei), 'utf8');
  const vorlage = fs.readFileSync(path.join(WURZEL, VORLAGE), 'utf8');

  // --- 1. Shared Header und Footer
  const cssDa = seite.includes('shared-header-footer.css');
  const kopfGleich = block(seite, 'header') === block(vorlage, 'header');
  const fussGleich = block(seite, 'footer') === block(vorlage, 'footer');
  melde('Shared Header und Footer', cssDa && kopfGleich && fussGleich,
    `Stylesheet ${cssDa ? 'geladen' : 'FEHLT'}, Header ${kopfGleich ? 'gleich' : 'ABWEICHEND'}, Footer ${fussGleich ? 'gleich' : 'ABWEICHEND'}`);

  // --- 2. Assetpfade
  const pfade = [...new Set((seite.match(/(?:src|href)="(assets\/[^"]+)"/g) || [])
    .map(s => s.replace(/.*="/, '').replace('"', '')))];
  const fehlend = pfade.filter(p => !fs.existsSync(path.join(WURZEL, p)));
  melde('Assetpfade vorhanden', fehlend.length === 0,
    fehlend.length ? fehlend.join(', ') : `${pfade.length} Pfade, alle vorhanden`);

  // --- 3. Trennlinien, styleguide 21.5
  const anzSektionen = (seite.match(/<section class="section/g) || []).length;
  const anzLinien = (seite.match(/class="section-divider"/g) || []).length;
  melde('Trennlinien (21.5)', anzLinien === anzSektionen - 1,
    `${anzSektionen} Sektionen, ${anzLinien} Trennlinien, Soll ${anzSektionen - 1}`);

  // --- 4./5. Texte und Links gegen die Quellseite
  // Freigegebene Abweichungen, je Seite. Jede Zeile ist eine ausdrueckliche
  // Entscheidung des Nutzers und in decision_log.md belegt.
  const freigabeDatei = path.join(__dirname, 'freigaben', datei.replace(/\.html$/, '.json'));
  const frei = fs.existsSync(freigabeDatei) ? JSON.parse(fs.readFileSync(freigabeDatei, 'utf8')) : { texte: [], linksOhne: [] };

  if (quelle) {
    const q = fs.readFileSync(path.join(WURZEL, quelle), 'utf8');
    const tq = textstuecke(q).join(' ||| ');
    const ts = textstuecke(seite);
    const fremd = ts.filter(t => !tq.includes(t) && !(frei.texte || []).includes(t));
    melde('Keine fremden Texte', fremd.length === 0,
      fremd.length ? fremd.slice(0, 8).map(t => '"' + t.slice(0, 60) + '"').join('; ')
                   : `kein Textstueck ausserhalb der Quellseite${(frei.texte || []).length ? ` (${frei.texte.length} freigegeben)` : ''}`);

    const ls = links(seite).join('|'), lq = links(q);
    const fehlendeLinks = [...new Set(lq.filter(h => !ls.includes(h) && !h.startsWith('#') && !(frei.linksOhne || []).includes(h)))];
    melde('Links wie in der Quelle', fehlendeLinks.length === 0,
      fehlendeLinks.length ? 'nicht uebernommen: ' + fehlendeLinks.join(', ') : links(seite).join(', ') || 'keine Inhaltslinks');
  }

  // --- 6. Sektionskoepfe vollstaendig
  const luecken = [];
  const reSek = /<section class="section[^"]*"[^>]*id="([a-z-]+)"([\s\S]*?)<\/section>/g;
  let m;
  while ((m = reSek.exec(seite))) {
    const id = m[1];
    const kopf = m[2].split(/<(?:ol|ul|div class="content-grid|div class="media-split|div class="pair|figure)/)[0];
    const fehlt = [];
    if (!/<div class="kicker">/.test(kopf)) fehlt.push('Kicker');
    if (!/<h[12]>/.test(kopf)) fehlt.push('Titel');
    if (!/<p class="sub">/.test(kopf)) fehlt.push('Subline');
    if (fehlt.length) luecken.push(`${id}: ${fehlt.join(', ')}`);
  }
  melde('Sektionskoepfe vollstaendig', luecken.length === 0,
    luecken.length ? luecken.join(' | ') : 'Kicker, Titel und Subline in jeder Sektion');

  // --- 7. bis 10. im Browser
  const { s, port } = await server();
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
  const abwWerte = [], abwEinzug = [], abwUeberlauf = [], meldungen = [];

  for (const w of BREITEN) {
    const page = await browser.newPage({ viewport: { width: w, height: 1000 } });
    page.on('pageerror', e => meldungen.push(`${w}px JS: ${e.message}`));
    page.on('requestfailed', r => meldungen.push(`${w}px Fehlantwort: ${r.url()}`));
    page.on('console', c => { if (c.type() === 'error') meldungen.push(`${w}px Konsole: ${c.text()}`); });
    await page.goto(`http://127.0.0.1:${port}/${datei}`, { waitUntil: 'networkidle' });
    await page.waitForTimeout(400);

    const d = await page.evaluate(({ BLOECKE, SOLL }) => {
      const breite = sel => { const e = document.querySelector(sel); return e ? Math.round(e.getBoundingClientRect().width) : null; };
      const kasten = sel => { const e = document.querySelector(sel); if (!e) return null; const b = e.getBoundingClientRect(); return [Math.round(b.left), Math.round(b.right), Math.round(b.width)]; };
      const inner = document.querySelector('.section:not(#hero) .section-inner');
      const ib = inner ? inner.getBoundingClientRect() : null;
      const kicker = document.querySelector('.section:not(#hero) .kicker');
      return {
        ueberlauf: document.documentElement.scrollWidth - document.documentElement.clientWidth,
        innerBreite: ib ? Math.round(ib.width) : null,
        kopfkante: kicker ? Math.round(kicker.getBoundingClientRect().left) : null,
        bloecke: BLOECKE.map(([n, sel]) => [n, kasten(sel)]),
        karte: breite('.analysis-intro-cards .panel'),
        listeneintrag: breite('.num-list li'),
        bild: breite('.section-photo'),
        textspalte: breite('.media-split > .media-copy'),
        sublinen: [...document.querySelectorAll('.section:not(#hero) .sub')].map(e => [
          e.closest('section').id,
          !!e.closest('.definition-intro'),
          Math.round(e.getBoundingClientRect().width)
        ]),
        faqKnopf: breite('.faq-item summary'),
        iconRahmen: breite('.module-icon-frame'),
        icon: breite('.module-icon')
      };
    }, { BLOECKE, SOLL });

    if (d.ueberlauf !== 0) abwUeberlauf.push(`${w}px: ${d.ueberlauf}`);

    if (w >= 901) {
      // Sollbreite des Inhalts: 1300, aber hoechstens section-inner minus zweimal Einzug
      const sollInhalt = Math.min(SOLL.inhalt, d.innerBreite - 2 * SOLL.einzug);
      const sollEinzug = Math.max(SOLL.einzug, Math.round((d.innerBreite - SOLL.inhalt) / 2));
      const voll = sollInhalt === SOLL.inhalt;

      for (const [name, k] of d.bloecke) {
        if (!k) continue;
        const [l, , br] = k;
        if (Math.abs(br - sollInhalt) > 2 && name !== 'Fliesstext') abwWerte.push(`${w}px ${name}: ${br} statt ${sollInhalt}`);
        if (Math.abs(l - d.kopfkante - sollEinzug) > 2) abwEinzug.push(`${w}px ${name}: Einzug ${l - d.kopfkante} statt ${sollEinzug}`);
      }
      // abgeleitete Werte nur pruefen, wo der Inhalt die vollen 1300 hat
      const paare = [['Karte', d.karte, SOLL.karte], ['Listeneintrag', d.listeneintrag, SOLL.listeneintrag],
                     ['Textspalte', d.textspalte, SOLL.textspalte]];
      if (voll) for (const [n, ist, soll] of paare)
        if (ist !== null && Math.abs(ist - soll) > 2) abwWerte.push(`${w}px ${n}: ${ist} statt ${soll}`);
      // diese gelten bei jeder Breite ab 901
      for (const [n, ist, soll] of [['Bild', d.bild, SOLL.bild],
                                    ['Icon-Rahmen', d.iconRahmen, SOLL.iconRahmen], ['Icon', d.icon, SOLL.icon]])
        if (ist !== null && Math.abs(ist - soll) > 2) abwWerte.push(`${w}px ${n}: ${ist} statt ${soll}`);
      for (const [id, inDefinition, ist] of d.sublinen) {
        const soll = inDefinition ? SOLL.sublineDefinition : SOLL.subline;
        if (Math.abs(ist - soll) > 2) abwWerte.push(`${w}px Subline ${id}: ${ist} statt ${soll}`);
      }
    }
    await page.close();
  }

  // Reduced Motion
  const rm = await browser.newPage({ viewport: { width: 1440, height: 900 }, reducedMotion: 'reduce' });
  rm.on('pageerror', e => meldungen.push(`reduced-motion JS: ${e.message}`));
  await rm.goto(`http://127.0.0.1:${port}/${datei}`, { waitUntil: 'networkidle' });
  await rm.waitForTimeout(400);
  await rm.close();
  await browser.close();
  s.close();

  melde('Werte aus Styleguide 21', abwWerte.length === 0,
    abwWerte.length ? abwWerte.join(' | ') : 'alle Bausteine auf Soll, 1100 bis 2560 px');
  melde('Einzug gleich in jedem Block', abwEinzug.length === 0,
    abwEinzug.length ? abwEinzug.join(' | ') : `${SOLL.einzug} px Mindesteinzug eingehalten`);
  melde('Kein waagerechter Ueberlauf', abwUeberlauf.length === 0,
    abwUeberlauf.length ? abwUeberlauf.join(' | ') : `0 bei ${BREITEN.join(', ')} px`);
  melde('Konsole und Antworten sauber', meldungen.length === 0,
    meldungen.length ? meldungen.slice(0, 6).join(' | ') : 'keine Fehler, keine Fehlantworten');

  // ---------------------------------------------------------------- Ausgabe
  const breiteName = Math.max(...ergebnisse.map(e => e.regel.length));
  console.log(`\nPflichtpruefung  homepage/${datei}` + (quelle ? `  gegen homepage/${quelle}` : '') + '\n');
  let offen = 0;
  for (const e of ergebnisse) {
    if (!e.bestanden) offen++;
    console.log(`  ${e.bestanden ? 'BESTANDEN ' : 'ABWEICHUNG'}  ${e.regel.padEnd(breiteName)}  ${e.text}`);
  }
  console.log(`\n  ${offen === 0 ? 'Alle Regeln bestanden.' : offen + ' Regel(n) abweichend.'}\n`);
  process.exit(offen === 0 ? 0 : 1);
})();
