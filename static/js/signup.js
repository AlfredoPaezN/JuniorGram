function hideStepOne(stepOne){
    return stepOne.classList.add('hide-content')
 }

function showStepTwo(stepTwo){
    return stepTwo.classList.remove('hide-content')
 }

function showSubmitButton(btnSubmit){
    return btnSubmit.classList.remove('hide-content')
 }

 function hideNextButton(btnNext){
    return btnNext.classList.add('hide-content')
 }
 
function handleForm(){
    
    let stepOne = document.getElementById('step-one');
    let stepTwo = document.getElementById('step-two');
    let btnNext = document.getElementById('btn-next');
    let btnSubmit = document.getElementById('btn-submit');


    btnNext.addEventListener('click', function(e){
            e.preventDefault()
            hideStepOne(stepOne)
            showStepTwo(stepTwo)
            showSubmitButton(btnSubmit)
            hideNextButton(btnNext)
        }
    )
 }
 

 document.addEventListener("DOMContentLoaded", handleForm(), false)