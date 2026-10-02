import json,re,sys,pathlib
HERE=pathlib.Path(__file__).resolve().parent
BASE=(HERE/"base.html").read_text(encoding='utf-8')
OUT=HERE.parent/"paginas"
OUT.mkdir(exist_ok=True)

def build(slug, cfg, title):
    js="var CONFIG = "+json.dumps(cfg,ensure_ascii=False,indent=2)+";"
    html=re.sub(r'/\*CONFIG-INICIO\*/.*?/\*CONFIG-FIM\*/',
                '/*CONFIG-INICIO*/\n'+js.replace('\\','\\\\')+'\n/*CONFIG-FIM*/',
                BASE,flags=re.S,count=1)
    html=re.sub(r'<title>.*?</title>', '<title>'+title+'</title>', html, count=1)
    assert '__CONFIG__' not in html
    p=OUT/(slug+".html"); p.write_text(html,encoding='utf-8'); print("ok",p.name,len(html),"bytes")
    return p

def gen_pair(slug, base_cfg, site_over, link_over, nome):
    site=dict(base_cfg); site.update(site_over)
    link=dict(base_cfg); link.update(link_over)
    build(slug+"-site", site, nome+" — Site")
    build(slug+"-link", link, nome+" — Links")

if __name__=="__main__":
    exec(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'))
