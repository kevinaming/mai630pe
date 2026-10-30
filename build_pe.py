"""MAI 630 PE: the Office Hours site with a game-style look (green 3D buttons, rounded cards, round font).
Same phrases, voice, player and assistant: the page is built from ../officehours, only the look changes.
Run after any change to Office Hours: python3 build_pe.py"""
import os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OH = os.path.join(HERE, "..", "officehours")

THEME = r"""
/* ===== MAI 630 PE look: dark slate, lime-green 3D buttons, sky-blue secondary, round heavy type ===== */
:root {
  --bg: #131F24; --surface: #1B2A31; --ink: #F1F7FB; --muted: #8DA2AC;
  --line: #37464F; --chip: #22343C; --es: #BFD0D8;
  --red: #93D333;                    /* the accent everywhere (it was red): lime green */
  --green: #93D333; --green-d: #79B933; --on-green: #131F24;
  --blue: #49C0F8; --blue-d: #1899D6; --on-blue: #0E1A1F;
  --danger: #FF4B4B; --danger-d: #D93A3A;
  --gold: #FFC800;
  --navy: #1CB0F6;
  --display: "Nunito", "Arial Rounded MT Bold", "Helvetica Neue", Arial, sans-serif;
  --body: "Nunito", "Segoe UI", Verdana, sans-serif;
}
body { font-weight: 600 }
body::before { background: var(--bg) }
h1, .tile .t, .np-h, .sheet-head h2, .chat-head h2 { font-weight: 900; letter-spacing: -.01em }
.eyebrow, .sheet h3, .stage-title { color: var(--green); font-weight: 900 }

/* 3D buttons: a 2px border plus a solid 2px drop below; pressing pushes them down */
.navbtn, .toggle, .drop-head, .act, .chip, .tbtn, .close, .tile, .hello .ex, .send, .fab, .fab-chat, .stage-x, .hit {
  border: 2px solid var(--line); box-shadow: 0 2px 0 var(--line); transition: transform .08s, box-shadow .08s, background .15s, border-color .15s }
.navbtn:active, .toggle:active, .drop-head:active, .act:active, .chip:active, .tbtn:active, .close:active, .tile:active:not(:disabled),
.hello .ex:active, .send:active, .fab:active, .fab-chat:active, .stage-x:active, .hit:active { transform: translateY(2px); box-shadow: none }

/* top bar */
.bar { background: rgba(19, 31, 36, .9); border-bottom: 2px solid var(--line) }
.navbtn { background: transparent; color: var(--blue); border-radius: 14px; text-transform: uppercase; letter-spacing: .06em; font-weight: 900; font-size: 13px }
.navbtn:hover { background: var(--chip) }
.crumb { font-weight: 800 }
.toggle, .topic-head .toggle { background: transparent; color: var(--ink); border-radius: 12px; font-weight: 800 }
.toggle[aria-pressed="true"], .topic-head .toggle[aria-pressed="true"] { background: rgba(73, 192, 248, .14); color: var(--blue); border-color: var(--blue-d); box-shadow: 0 2px 0 var(--blue-d) }
.drop-head { border-radius: 12px; font-weight: 800; background: transparent }
.drop.open .drop-head { background: var(--surface); border-color: var(--line); border-radius: 12px 12px 0 0; box-shadow: none }
.drop-list { background: var(--surface); border: 2px solid var(--line); border-top: 0; border-radius: 0 0 12px 12px }
.drop-item { color: var(--muted); font-weight: 700 }
.drop-item.on { color: var(--blue) }
.drop-item:hover, .drop-item:focus-visible { color: var(--ink) }
#barTopic { background: rgba(19, 31, 36, .9); border-bottom: 2px solid var(--line) }
.chip { background: transparent; color: var(--ink); border-radius: 12px; font-weight: 800 }
.chip[aria-current="true"] { background: rgba(73, 192, 248, .14); color: var(--blue); border-color: var(--blue-d); box-shadow: 0 2px 0 var(--blue-d) }

/* home tiles and phrase cards */
.tile { border-radius: 18px; background: var(--bg) }
.tile:hover:not(:disabled) { border-color: var(--line); background: var(--surface); transform: none }
.tile .s, .tile .n { font-weight: 600 }
.tag { background: rgba(147, 211, 51, .14); color: var(--green); font-weight: 900 }
.card { border: 2px solid var(--line); border-radius: 18px; box-shadow: 0 2px 0 var(--line); background: var(--bg) }
.ask { background: var(--surface); border-radius: 14px }
.ask .lbl, .ans-lbl { color: var(--muted); font-weight: 900 }
.en { font-weight: 800 }
.es { border-left-color: var(--blue) }
.card.reading { border-color: var(--green); box-shadow: 0 2px 0 var(--green-d), 0 0 0 3px rgba(147, 211, 51, .18) }
@keyframes flash { 0%, 40% { border-color: var(--green); box-shadow: 0 0 0 4px rgba(147, 211, 51, .25) } 100% { border-color: var(--line); box-shadow: 0 2px 0 var(--line) } }

/* buttons: Listen is the green primary, the rest are outlined blue-text secondaries */
.act { background: transparent; color: var(--blue); border-radius: 14px; text-transform: uppercase; letter-spacing: .05em; font-weight: 900; font-size: 14px }
.act:hover { border-color: var(--line); background: var(--chip) }
.act.play { background: var(--green); color: var(--on-green); border-color: var(--green); box-shadow: 0 4px 0 var(--green-d) }
.act.play:hover { background: #A5E04A; border-color: #A5E04A }
.act.play:active { transform: translateY(4px); box-shadow: none }
.act.stopping, .sel-say button.stopping { background: var(--danger); color: #fff; border-color: var(--danger); box-shadow: 0 4px 0 var(--danger-d) }
.next .act.play { box-shadow: 0 4px 0 var(--green-d) }

/* "next topic" window */
.np-card { border: 2px solid var(--line); border-radius: 20px; box-shadow: 0 4px 0 var(--line), 0 18px 50px rgba(0,0,0,.5) }

/* the player: a slate footer with a green play button and a thick progress track */
.reader-bar { background: var(--surface); color: var(--ink); border: 2px solid var(--line); border-radius: 22px; box-shadow: 0 4px 0 var(--line), 0 10px 30px rgba(0,0,0,.45) }
.reader-bar button { color: var(--ink) }
.reader-bar button:hover { background: var(--chip) }
.reader-bar #readerPlay { background: var(--green); color: var(--on-green); box-shadow: 0 4px 0 var(--green-d) }
.reader-bar #readerPlay:active { transform: translateY(4px); box-shadow: none }
.reader-bar #readerStop { background: transparent; color: var(--danger) }
.reader-bar .rb-count { color: var(--green); text-transform: uppercase; letter-spacing: .06em; font-weight: 900; font-size: 14px }
.rb-track { gap: 4px }
.rb-track button { height: 18px }
.rb-track button::after { top: 4px; height: 10px; border-radius: 6px; background: var(--line) }
.rb-track button.done::after { background: var(--green) }
.rb-track button.now::after { top: 4px; height: 10px; background: var(--line) }
.rb-track button i { top: 4px; height: 10px; border-radius: 6px; background: var(--green); box-shadow: inset 0 3px 0 rgba(255, 255, 255, .28) }
.rb-track button:hover::after { background: #4A5C66 }

/* full screen */
.stage { background: var(--bg) }
.stage-x { background: transparent; color: var(--muted); border-radius: 14px }
.en.karaoke .w.cur { color: var(--green) }

/* floating buttons, menu, search, assistant */
.fab { background: var(--green); color: var(--on-green); border-color: var(--green); box-shadow: 0 4px 0 var(--green-d); text-transform: uppercase; letter-spacing: .05em; font-weight: 900; border-radius: 16px }
.fab:active { transform: translateY(4px); box-shadow: none }
.fab-chat { background: var(--blue); color: var(--on-blue); border-color: var(--blue); box-shadow: 0 4px 0 var(--blue-d); text-transform: uppercase; letter-spacing: .05em; font-weight: 900; border-radius: 16px }
.fab-chat:active { transform: translateY(4px); box-shadow: none }
.close { background: transparent; color: var(--blue); border-radius: 14px; text-transform: uppercase; font-weight: 900; font-size: 13px }
.tbtn { background: var(--bg); border-radius: 14px; font-weight: 800 }
.tbtn[aria-current="true"] { border-color: var(--blue-d); color: var(--blue); background: rgba(73, 192, 248, .1); box-shadow: 0 2px 0 var(--blue-d) }
.qlist { border-left-color: var(--line) }
.qbtn { font-weight: 700 }
.qbtn.now { color: var(--green); background: var(--surface) }
.search, .composer textarea { border: 2px solid var(--line); border-radius: 14px; background: var(--surface); font-weight: 600 }
.search:focus, .composer textarea:focus { outline: none; border-color: var(--blue) }
.hit { background: var(--bg); border-radius: 14px }
.hit mark { background: var(--gold); color: #131F24 }
.msg-me { background: var(--blue); color: var(--on-blue); font-weight: 700 }
.msg-bot { border: 2px solid var(--line); border-radius: 16px; background: var(--bg) }
.hello .ex { background: transparent; border-radius: 14px; font-weight: 700 }
.send { background: var(--green); color: var(--on-green); border-color: var(--green); box-shadow: 0 4px 0 var(--green-d); border-radius: 14px; text-transform: uppercase; font-weight: 900 }
.send.stop { background: var(--muted); border-color: var(--muted); box-shadow: 0 4px 0 var(--line) }
.pin[aria-pressed="true"] { background: rgba(73, 192, 248, .14); color: var(--blue); border-color: var(--blue-d) }
.sel-say { background: var(--surface); border: 2px solid var(--line) }
.sel-say button { color: var(--blue); font-weight: 900 }
.swipe-hint { background: var(--blue); color: var(--on-blue) }
.pull-hint { background: var(--green); color: var(--on-green) }
.hidden-en { filter: blur(8px) }
button:focus-visible, select:focus-visible { outline-color: var(--blue) }
@media (prefers-reduced-motion: reduce) { .navbtn, .toggle, .act, .chip, .tbtn, .tile, .fab, .fab-chat { transition: none } }
"""

html = open(os.path.join(OH, "index.html")).read()
def rep(a, b):
    global html
    assert html.count(a) == 1, a[:60]
    html = html.replace(a, b)
rep("<title>MAI 630 Office Hours</title>", "<title>MAI 630 PE</title>")
rep("family=Atkinson+Hyperlegible:wght@400;700&family=Archivo:wght@600;800&display=swap", "family=Nunito:wght@600;700;800;900&display=swap")
rep('crumb.textContent = "MAI 630 · Office Hours";', 'crumb.textContent = "MAI 630 PE";')
rep("<h1>Office Hours: qué decir en Zoom</h1>", "<h1>MAI 630 PE: qué decir en Zoom</h1>")
i = html.index("</style>")
html = html[:i] + THEME + html[i:]
open(os.path.join(HERE, "index.html"), "w").write(html)
shutil.copy(os.path.join(OH, "data.js"), os.path.join(HERE, "data.js"))
print("written index.html", len(html), "bytes + data.js")
