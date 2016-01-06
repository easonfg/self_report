/* set global variable i */

var i=0;

function increment(){
i +=1;                         /* function for automatic increament of feild's "Name" attribute*/
}

/*
---------------------------------------------

function to remove fom elements dynamically
---------------------------------------------

*/

function removeElement(parentDiv, childDiv){


     if (childDiv == parentDiv) {
          alert("The parent div cannot be removed.");
     }
     else if (document.getElementById(childDiv)) {
          var child = document.getElementById(childDiv);
          var parent = document.getElementById(parentDiv);
          parent.removeChild(child);
     }
     else {
          alert("Child div has already been removed or does not exist.");
          return false;
     }
}


 /*
 ----------------------------------------------------------------------------

 functions that will be called upon, when user click on the Name text field

 ---------------------------------------------------------------------------
 */
function SymptomsFunction()
{
var r=document.createElement('span');
var y = document.createElement("INPUT");
y.setAttribute("type", "text");
y.setAttribute("placeholder","Symptoms");
var g = document.createElement("span");
//g.setAttribute("src", "delete.png");
g.className ="glyphicon glyphicon-remove-circle";
increment();
y.setAttribute("Name","textelement_"+i);
r.appendChild(y);
g.setAttribute("onclick", "removeElement('myForm','id_"+ i +"')");
r.appendChild(g);
r.setAttribute("id", "id_"+i);
document.getElementById("myForm").appendChild(r);
}


/*
-----------------------------------------------------------------------------

functions  that will be called upon, when user click on the Email text field

------------------------------------------------------------------------------
*/
function DiagnosisFunction()
{
var r=document.createElement('span');
var y = document.createElement("INPUT");
y.setAttribute("type", "text");
y.setAttribute("placeholder", "Diagnosis");
var g = document.createElement("span");
//g.setAttribute("src", "delete.png");
g.className ="glyphicon glyphicon-remove-circle";
increment();
y.setAttribute("Name","textelement_"+i);
r.appendChild(y);
g.setAttribute("onclick", "removeElement('myForm','id_"+ i +"')");
r.appendChild(g);
r.setAttribute("id", "id_"+i);
document.getElementById("myForm").appendChild(r);
}

/*
-----------------------------------------------------------------------------

functions  that will be called upon, when user click on the Contact text field

------------------------------------------------------------------------------
*/

function TreatmentFunction()
{
var r=document.createElement('span');
var y = document.createElement("INPUT");
y.setAttribute("type", "text");
y.setAttribute("placeholder", "Treatment");
var g = document.createElement("span");
//g.setAttribute("src", "delete.png");
g.className ="glyphicon glyphicon-remove-circle";
increment();
y.setAttribute("Name","textelement_"+i);
r.appendChild(y);
g.setAttribute("onclick", "removeElement('myForm','id_"+ i +"')");
r.appendChild(g);
r.setAttribute("id", "id_"+i);
document.getElementById("myForm").appendChild(r);
}

/*
-----------------------------------------------------------------------------

functions  that will be called upon, when user click on the Messege textarea field

------------------------------------------------------------------------------
*/

function textareaFunction()
{
var r=document.createElement('span');

var y = document.createElement("TEXTAREA");
y.setAttribute("cols", "17");
y.setAttribute("placeholder", "message..");
var g = document.createElement("span");
//g.setAttribute("src", "delete.png");
g.className ="glyphicon glyphicon-remove-circle";
increment();
y.setAttribute("Name","textelement_"+i);
r.appendChild(y);
g.setAttribute("onclick", "removeElement('myForm','id_"+ i +"')");
r.appendChild(g);
r.setAttribute("id", "id_"+i);
document.getElementById("myForm").appendChild(r);

}

/*
-----------------------------------------------------------------------------

functions  that will be called upon, when user click on the Reset Button

------------------------------------------------------------------------------
*/
function resetElements(){
document.getElementById('myForm').innerHTML = '';
}
