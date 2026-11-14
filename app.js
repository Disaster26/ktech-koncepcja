(function(){
  var d=document;
  // rok
  var r=d.getElementById('rok'); if(r) r.textContent=new Date().getFullYear();

  // menu mobilne
  var b=d.querySelector('.burger'), m=d.getElementById('menu-mob');
  function zamknij(){b.setAttribute('aria-expanded','false');m.hidden=true;}
  if(b&&m){
    b.addEventListener('click',function(){var o=b.getAttribute('aria-expanded')==='true';b.setAttribute('aria-expanded',String(!o));m.hidden=o;});
    m.addEventListener('click',function(e){if(e.target.closest('a'))zamknij();});
    d.addEventListener('keydown',function(e){if(e.key==='Escape')zamknij();});
  }

  // przeciąganie myszą (palec działa natywnie)
  function ciagnij(el){
    var x0=0,s0=0,ruch=false,dn=false;
    el.addEventListener('pointerdown',function(e){if(e.pointerType!=='mouse'||e.button!==0)return;dn=true;ruch=false;x0=e.clientX;s0=el.scrollLeft;});
    window.addEventListener('pointermove',function(e){if(!dn)return;var dx=e.clientX-x0;if(Math.abs(dx)>4){ruch=true;el.classList.add('ciag');}if(ruch){el.scrollLeft=s0-dx;e.preventDefault();}});
    var ldx=0;window.addEventListener('pointerup',function(e){if(!dn)return;dn=false;if(ruch){dociagnij(el,e.clientX-x0);setTimeout(function(){el.classList.remove('ciag');},450);}});
    el.addEventListener('click',function(e){if(ruch){e.preventDefault();e.stopPropagation();ruch=false;}},true);
    el.addEventListener('dragstart',function(e){e.preventDefault();});
  }
  function krok(el){var c=el.firstElementChild;if(!c)return el.clientWidth;var g=parseFloat(getComputedStyle(el).columnGap)||0;return c.getBoundingClientRect().width+g;}
  function dociagnij(el,dx){var k=krok(el),q=el.scrollLeft/k,i=Math.abs(dx)>40?(dx<0?Math.ceil(q):Math.floor(q)):Math.round(q);el.scrollTo({left:i*k,behavior:'smooth'});}

  // karuzele w kartach
  d.querySelectorAll('.sw').forEach(function(sw){
    var t=sw.querySelector('.sw-tor'),n=sw.querySelector('.sw-n'),of=sw.getAttribute('data-of')||'/',ile=t.children.length;
    ciagnij(t);
    function idx(){return Math.round(t.scrollLeft/t.clientWidth);}
    function idz(i){i=(i+ile)%ile;t.scrollTo({left:i*t.clientWidth,behavior:'smooth'});}
    sw.querySelector('.sw-prev').addEventListener('click',function(){idz(idx()-1);});
    sw.querySelector('.sw-next').addEventListener('click',function(){idz(idx()+1);});
    t.addEventListener('keydown',function(e){if(e.key==='ArrowRight'){idz(idx()+1);e.preventDefault();}if(e.key==='ArrowLeft'){idz(idx()-1);e.preventDefault();}});
    var raf;t.addEventListener('scroll',function(){cancelAnimationFrame(raf);raf=requestAnimationFrame(function(){n.textContent=(idx()+1)+' '+of+' '+ile;});},{passive:true});
  });

  // katalog
  var kat=d.querySelector('.kat');
  if(kat){
    ciagnij(kat);
    d.querySelectorAll('[data-kat]').forEach(function(btn){btn.addEventListener('click',function(){kat.scrollBy({left:krok(kat)*2*parseInt(btn.getAttribute('data-kat'),10),behavior:'smooth'});});});
    kat.addEventListener('keydown',function(e){if(e.key==='ArrowRight'){kat.scrollBy({left:krok(kat),behavior:'smooth'});e.preventDefault();}if(e.key==='ArrowLeft'){kat.scrollBy({left:-krok(kat),behavior:'smooth'});e.preventDefault();}});
  }

  // aktywny punkt menu
  var linki=[].slice.call(d.querySelectorAll('.nav a'));
  if('IntersectionObserver' in window&&linki.length){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){linki.forEach(function(a){a.classList.toggle('akt',a.getAttribute('href')==='#'+e.target.id);});}});},{rootMargin:'-45% 0px -50% 0px'});
    ['oferta','maszyny','wyroby','wycena','kontakt'].forEach(function(id){var s=d.getElementById(id);if(s)io.observe(s);});
    var start=d.getElementById('start');
    if(start)new IntersectionObserver(function(es){if(es[0].isIntersecting)linki.forEach(function(a){a.classList.remove('akt');});},{rootMargin:'-45% 0px -50% 0px'}).observe(start);
  }

  // dolny pasek po przewinięciu za przycisk hero
  var p=d.getElementById('pasek'),cta=d.getElementById('hero-cta'),wyc=d.getElementById('wycena');
  if(p&&cta&&'IntersectionObserver' in window){
    var zaCta=false,naWyc=false;
    function ustaw(){var w=zaCta&&!naWyc;p.classList.toggle('widac',w);p.setAttribute('aria-hidden',String(!w));p.querySelectorAll('a').forEach(function(a){a.tabIndex=w?0:-1;});}
    new IntersectionObserver(function(es){zaCta=!es[0].isIntersecting&&es[0].boundingClientRect.top<0;ustaw();}).observe(cta);
    new IntersectionObserver(function(es){naWyc=es[0].isIntersecting;ustaw();},{threshold:.15}).observe(d.getElementById('form'));
  }

  // formularz pokazowy
  var f=d.getElementById('form'),pl=d.getElementById('f-plik'),pn=d.getElementById('plik-n');
  if(pl&&pn){var dom=pn.textContent;pl.addEventListener('change',function(){pn.textContent=pl.files.length?[].map.call(pl.files,function(x){return x.name;}).join(', '):dom;});}
  if(f)f.addEventListener('submit',function(e){e.preventDefault();var i=d.getElementById('form-info');i.hidden=false;i.scrollIntoView({block:'nearest',behavior:'smooth'});});

  // baner cookies (mapa Google)
  var ck=d.getElementById('cookies'),zg=null;
  try{zg=localStorage.getItem('ktech-zgoda');}catch(e){}
  if(ck&&zg===null){
    var pok=function(){if(window.scrollY>200){ck.hidden=false;window.removeEventListener('scroll',pok);}};window.addEventListener('scroll',pok,{passive:true});
    ck.addEventListener('click',function(e){var bt=e.target.closest('[data-ck]');if(!bt)return;try{localStorage.setItem('ktech-zgoda',bt.getAttribute('data-ck'));}catch(er){}ck.hidden=true;});
  }

  // tabela wymiarów: filtr po średnicy
  var fi=d.getElementById('filtr-d'),tb=d.getElementById('tab-wym');
  if(fi&&tb){
    var rows=[].slice.call(tb.tBodies[0].rows),info=d.getElementById('filtr-info'),brak=d.getElementById('filtr-brak'),czysc=d.getElementById('filtr-x');
    var num=function(v){return parseFloat(String(v).replace(/[()]/g,' ').trim().split(/\s+/).pop().replace(',','.'));};
    var filtruj=function(){
      var v=parseFloat(fi.value.replace(',','.')),n=0;
      rows.forEach(function(r){
        var ok=isNaN(v);
        if(!ok){var d1=num(r.getAttribute('data-d1')),d3=num(r.getAttribute('data-d3')),d2=num(r.getAttribute('data-d2'));ok=Math.abs(d1-v)<=10||Math.abs(d3-v)<=10||Math.abs(d2-v)<=10;}
        r.hidden=!ok;if(ok)n++;
      });
      info.textContent=isNaN(v)?rows.length+' rozmiarów w typoszeregu':'Pasuje: '+n+' z '+rows.length+' (średnica ±10 mm)';
      brak.hidden=!(n===0);czysc.hidden=isNaN(v);
    };
    fi.addEventListener('input',filtruj);
    czysc.addEventListener('click',function(){fi.value='';filtruj();fi.focus();});
    filtruj();
  }
})();
