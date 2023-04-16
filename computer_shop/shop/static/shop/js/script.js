// back to top with button
function backToTop(){
    let button = $('.back-to-top');
    button.fadeOut();
    $(window).on('scroll', () => {
        if ($(window).scrollTop() >= 500 && $(window).scrollTop() != null){
            button.fadeIn();
        } else {
            button.fadeOut();
        }
    });
    button.on('click', (e) => {
        e.preventDefault();
        $('html').animate({scrollTop: 0}, 500);
    });
}

backToTop();

// loader
let mask = document.querySelector('.mask');
window.addEventListener('load', () => {
    mask.classList.add('hide');
    setTimeout(() => {
        mask.remove();
    }, 600);
});

//info-card
let cards = document.querySelectorAll('.info-card');
for(let item = 0; item < cards.length; item++){
    cards[item].addEventListener('click', () => {
        const cardImg = document.getElementsByClassName('card-img')[item];
        const cardText = document.getElementsByClassName('card-text')[item];
        
        const backGround = document.createElement("div");
        backGround.className = "back-ground";
        document.body.appendChild(backGround);

        const infoCardBig = document.createElement("div");
        infoCardBig.className = "info-card-big";
        document.body.appendChild(infoCardBig);

        const cardImgBig = document.createElement("div");
        cardImgBig.className = "card-img-big";
        cardImgBig.innerHTML = cardImg.innerHTML;
        infoCardBig.appendChild(cardImgBig);

        const cardTextBig = document.createElement("div");
        cardTextBig.className = "card-text-big";
        cardTextBig.innerText = cardText.innerHTML;
        infoCardBig.appendChild(cardTextBig);

        const close_a = document.createElement("div");
        close_a.className = "close";
        close_a.innerHTML = '<i class="fa-solid fa-xmark"></i>';
        infoCardBig.appendChild(close_a);

        let close = document.querySelector('.close');
        document.addEventListener('keydown', (e) =>{
            let key_close = e.key;
            if(key_close === "Escape"){
                infoCardBig.classList.add('hide');
                setTimeout(() => {
                    backGround.remove();
                    infoCardBig.remove();
                }, 300);
            }
        });
        close.addEventListener('click', () => {
            infoCardBig.classList.add('hide');
            setTimeout(() => {
                backGround.remove();
                infoCardBig.remove();
            }, 300);
        });
    });
}