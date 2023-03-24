const navbar = document.getElementsByClassName('topNavbar')[0]
const links = document.getElementsByClassName('NavLinks')[0]
const btn = document.getElementsByClassName('menu')[0]
const bar = document.getElementsByClassName('bar')[0]
const cross = document.getElementsByClassName('cross')[0]

btn.addEventListener('click',()=>{
    btn.classList.toggle('active');
    navbar.classList.toggle('active');
    links.classList.toggle('active');
    bar.classList.toggle('active');
    cross.classList.toggle('active');
});

const divbtn = document.getElementsByClassName('leftLogo')[0]
const sideLinks = document.getElementsByClassName('leftOption')[0]
divbtn.addEventListener('click',()=>{
    sideLinks.classList.toggle('active')
})