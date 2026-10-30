"""Builds the single-file version for the Claude artifact: page + phrases + course context (for the assistant).
Run: python3 build_artifact.py OUT.html"""
import json, os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
html = open(os.path.join(here, "index.html")).read()
data = open(os.path.join(here, "data.js")).read()
ctx = open(os.path.join(here, "..", "MAI630_Course_Context.md")).read()
# the artifact viewer adds its own document skeleton
html = html[html.index("<title>"):]
html = html.replace("</head>\n<body>\n", "").replace("</body>\n</html>\n", "")
html = html.replace('<script src="data.js"></script>',
                    "<script>\n" + data + "\nwindow.COURSE_CONTEXT = " + json.dumps(ctx, ensure_ascii=False) + ";\n</script>")
open(sys.argv[1], "w").write(html)
print("written", sys.argv[1], len(html), "bytes")
