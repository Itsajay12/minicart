let message = document.querySelector('.text-message');
let mouth = document.querySelector('.mouth');
let text = 'Welcome To Minicart 💖 !';
const speak = ()=>{
  mouth.style.animationPlayState = 'running';
  message.textContent = "";
  for(let i = 0;i< text.length; i++){
    setTimeout(()=>{
      message.textContent += text[i];
    },i*100);
    if(i == text.length -1){
      setTimeout(()=>{
        mouth.style.animationPlayState = 'paused';
      },i*100)
    }
  }

}
speak();
setInterval(speak,3000);