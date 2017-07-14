// functions declaration

function init () {
  allWords = data["data"];
  setStuff(allWords.pop());
}

function end () {
  var nextButton = document.getElementById('next-button');

  nextButton.innerHTML = 'Retry';
  nextButton.style.backgroundColor = '#0078e7';
}

function next () {
  var wordTried;
  var correctWords = wordsToFind.slice(0);
  var cwLen;
  var wrongId = [];

  // check previous
  for (var i = 0; i < wordsToFind.length; i++) {
    wordTried = document.getElementById('box' + i).value;
    cwLen = correctWords.length;
    correctWords = findWord(correctWords, wordTried);

    if(correctWords.length === cwLen) {
      wrongId.push(i);
    }
  }

  // show previous
  showLast(wrongId);

  // new words
  var words = allWords.pop();

  if (words)
    setStuff(words);
  else
    end();

  return false;  // so that the form is not submitted
}

function showLast(wrongId) {
  var lastKey = document.getElementById('keyword').innerHTML;
  document.getElementById('last-keyword').innerHTML = lastKey;
  var nb = wordsToFind.length;
  var lastContainer = document.getElementById('last-container');
  lastContainer.style.display = "block";

  for (var i = 0; i < nb; i++) {
    var element = document.getElementById('last' + i);
    element.innerHTML = wordsToFind[i];
  }

  for (i = nb; i < NB_BOXES; i++) {
    document.getElementById('last' + i).innerHTML = "";
  }

  if (wrongId.length === 0) {
    lastContainer.style.backgroundColor = "#9FB69F";
  }
  else {
    lastContainer.style.backgroundColor = "#D0B7C1";
  }
}

function findWord (refArray, b) {
  // Return refArray. if word is found, remove it.
  for (var i = 0; i < refArray.length; i++) {
    if (customCompare(refArray[i], b))
      refArray.splice(i, 1);
  }

  return refArray;
}

function customCompare(ref, b) {
  var rf1 = customShaping(ref);
  var rf2 = customShaping2(ref);
  b = customShaping(b);

  return rf1 === b || rf2 === b;
}

function customShaping(word) {
  word = word.toLowerCase();
  word = removeParenth(word);
  word = word.trim().replace(/\s+/g, " ");  // useless whitespace
  return word;
}

function customShaping2(word) {
  word = word.toLowerCase();
  word = word.replace(/[{()}]/g, "");
  word = word.trim().replace(/\s+/g, " ");  // useless whitespace
  return word;
}

function removeParenth(word) {
  var regExp = /(\([^)]+\))/;
  return word.replace(regExp, "");
}

function setStuff (words) {
  setLabel(words.shift());
  wordsToFind = words;
  setBoxes(words.length);
}

function setLabel (keyword) {
  document.getElementById('keyword').innerHTML = keyword;
}

function setBoxes (nb) {
  var i;

  if(nb === 0) {
    error('any word to test...');
  }
  // TO DO: if a single box, do not use a group of boxes

  var box = document.getElementById('box' + 0);
  box.style.display = 'block';
  box.value = "";

  for (i = NB_BOXES-1; i > NB_BOXES-nb; i--) {
    box = document.getElementById('box' + i);
    box.style.display = 'block';
    box.value = "";
  }

  for (i = 1; i < NB_BOXES+1-nb; i++) {
    document.getElementById('box' + i).style.display = 'none';
  }
}

function newOrContinue() {
  return false;
}

var NB_BOXES = 5;
var allWords;
var wordsToFind;
init();