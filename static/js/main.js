gsap.fromTo('.text-osnova',{opacity:1,scale:1},{scale:1.25,opacity:0,scrollTrigger:{trigger:'.text-osnova',start: 0*vh,end:100*vh,scrub:true}})
ScrollTrigger.matchMedia({
    "(max-width: 769px)": function() {
      gsap.to(['.no_div-block2-1', '.no_div-block2-2', '.no_div-block2-3', '.no_div-block2-4', '.no_div-block2-5', '.no_div-block2-6', '.Button__link'], {
        top: "0",
        duration: 0.6,
        stagger: 0.1,
        scrollTrigger: {
          trigger: '.no_div-block2-1',
          start:80*vhh,
          end:80*vhh
        }
      });

      gsap.fromTo('.imgBlock3__div-3', {width: "5%"}, {width: "70%",duration:.6, scrollTrigger: {trigger: '.imgBlock3__div-3', start: 145*vh,end:155*vh}});
      gsap.fromTo('.imgBlock3__img', {height: "100%"}, {height: "110%",duration:.5,delay:.5, scrollTrigger: {trigger: '.imgBlock3__img', start: 145*vh,end:155*vh}});
      gsap.to('.conteiner__block-3', {opacity:1,duration:.5, scrollTrigger: {trigger: '.conteiner__block-3', start: 145*vh,end:155*vh}});
      gsap.fromTo('.FAKE__SECTION3', {height: "100vh"}, {height: "0vh",duration:.1,delay:1, scrollTrigger: {trigger: '.imgBlock3__img', start: 145*vh,end:155*vh}});
    },
    "(min-width: 770px)": function() {
      gsap.to(['.no_div-block2-1', '.no_div-block2-2', '.no_div-block2-3', '.no_div-block2-4', '.no_div-block2-5', '.no_div-block2-6', '.Button__link'], {
        top: "0",
        duration: 0.6,
        stagger: 0.1,
        scrollTrigger: {
          trigger: '.no_div-block2-1',
          start:180*vhh,
          end:180*vhh
        }
      });

    gsap.fromTo('.imgBlock3__div-3', {width: "5%"}, {width: "70%",duration:.6,delay:.1, scrollTrigger: {trigger: '.imgBlock3__div-3', start: 305*vh,end:315*vh}});
    // gsap.fromTo('.imgBlock3__img', {height: "100%"}, {height: "110%",duration:.5,delay:.5, scrollTrigger: {trigger: '.imgBlock3__img', start: 305*vh,end:315*vh}});
    gsap.to('.conteiner__block-3', {opacity:1,duration:.5, scrollTrigger: {trigger: '.conteiner__block-3', start: 305*vh,end:315*vh}});
    gsap.fromTo('.FAKE__SECTION3', {height: "100vh"}, {height: "0vh",duration:.1,delay:1, scrollTrigger: {trigger: '.imgBlock3__img', start: 305*vh,end:315*vh}});

    }
  });

  gsap.to(".play-form", {rotation: 7,yoyo: true,repeat: -1,  duration: 1,    ease: "power1.inOut",yoyoEase: true  });
  document.querySelector('.div__go-video').addEventListener('mouseenter', () => {
    gsap.to(".play-form", { duration: .3,scale:1.3});
    gsap.to(".play-button", { duration: .3,scale:1.1});
  });

  document.querySelector('.div__go-video').addEventListener('mouseleave', () => {
    gsap.to(".play-form,.play-button", { duration: .5,scale:1});
  });



  const video = document.getElementById('videoo');
  const muteButton = document.getElementById('muteButton');
  const on = document.querySelector('.VKL');
  const off = document.querySelector('.OFF');
  video.addEventListener('ended', EndVideo);
  function PlayVideo(){
    document.querySelector(".DIV-VIDEO").style.display='flex';
    gsap.to(".DIV-VIDEO", {opacity: 1,duration: .1,delay:.5});
    gsap.to(".COSTILBLACK", {opacity: 1,duration: .5});
    gsap.to(".COSTILBLACK", {opacity: 0,duration:1,delay:2});
    setTimeout(() => {
        document.documentElement.style.overflow = 'hidden';
        document.body.style.overflow = 'hidden';
        video.play();
        document.querySelector('.header-osnova').style.display = 'none';
    }, 500);
  }
  function EndVideo(){
    gsap.to(".DIV-VIDEO", {opacity: 0,duration: .1,delay:.5});
    gsap.to(".COSTILBLACK", {opacity: 1,duration: .5});
    gsap.to(".COSTILBLACK", {opacity: 0,duration:1,delay:2});
    setTimeout(() => {
        document.documentElement.style.overflow = 'auto';
        document.body.style.overflow = 'auto';
        video.pause();
        video.currentTime = 0;
    }, 500);
    setTimeout(() => {
        document.querySelector(".DIV-VIDEO").style.display='none';
        document.querySelector('.header-osnova').style.display = 'block';
    }, 1000);
  }
  function toggleMute() {
    video.muted = !video.muted;
    if (video.muted) {
        on.style.display = 'none';
        off.style.display = 'block';
    } else {
        on.style.display = 'block';
        off.style.display = 'none';
    }
}