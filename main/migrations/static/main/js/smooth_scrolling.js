const anchors = document.querySelectorAll('a[href*="#"]')

for(let anchor of anchors){
    anchor.addEventListener("click", function(event){
        event.preventDefault();
        const blockID = anchor.getAttribute('href')
        document.querySelector('' + blockID).scrollIntoView({
            behavior: "smooth",
            block: "start"
        })
    })
}


function backToTop(){
 let button = $('.back-to-top');

 $(window).on('scroll', () => {
    if($(this).scrollTop()>= 50){
        button.fadeIn();
    }
    else{
        button.fadeOut();
    }
 });

 button.on('click', (e) => {
    e.preventDefault();
    $('html').animate({scrollTop: 0}, 1000);
 })
}

backToTop();