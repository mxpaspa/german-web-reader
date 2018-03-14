window.onLoad = function selectText() {

var els = document.getElementById('iframe');
var word = '';

els.addEventListener('click', function selectText(){
  // console.log('section made');
  word = window.getSelection().toString();
  console.log(word);
});
