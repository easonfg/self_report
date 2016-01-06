// Class to represent a row in the seat reservations grid
function condition_rows(name, init_conditions) {
    var self = this;
    //self.name = name;
    self.name = ko.observable(name);;
    self.condition = ko.observable(init_conditions);



    //self.formattedPrice = ko.computed(function() {
    //    var price = self.condition().price;
    //    return price ? "$" + price.toFixed(2) : "None";
    //});
}

// Overall viewmodel for this screen, along with initial state
function TimeSeqViewModel() {
    var self = this;


    // Non-editable catalog data - would come from the server
    self.availableConditions = [
        { cond_type: "Symptoms"},
        { cond_type: "Diagnosis"},
        { cond_type: "Treatment"}
    ];

    // Editable data
    self.cond_report = ko.observableArray([
        new condition_rows("", self.availableConditions[0]),
    ]);



//var dataset = [];
//
//
//function handleClick(event){
//    console.log(document.getElementById("descriptions").value)
//     console.log(dataset)
//    draw(document.getElementById("descriptions").value)
//    return false;
//}
//
//function draw(val){
//    d3.select("body").select("ul").append("li");
//    dataset.push(val);
//    var p = d3.select("body").selectAll("li")
//    .data(dataset)
//    .text(function(d,i){console.log(d,i); return i + ": " + d;})
//}

var dataset = {};

    // Computed data
    self.string_output = ko.computed(function() {
       var a = '';
       for (var i = 0; i < self.cond_report().length -1 ; i++) {
           a += self.cond_report()[i].name() + ' ';
          }
       //draw(self.cond_report()[0].name())
       return a;
    });


d3.select("#submit_data").on("click",function(){
        var plainJs = ko.toJS(self.cond_report());
        var jsonData = ko.toJSON(self.cond_report().slice(0,self.cond_report().length-1));
      console.log(plainJs)
      console.log(jsonData)

//$.post("/./file.html", jsonData, function(returnedData) {
//console.log('yay')
//})

 $.ajax({
   url: './FILE.php',
   type: 'post',
   contentType:'application/json',
   data: plainJs,
   dataType:'json',
   success: function(data){
     //On ajax success do this
     alert(data);
      console.log('yay')
      },
   error: function(xhr, ajaxOptions, thrownError) {
      //On error do this
      console.log('NOOOO')
    }
 });

})


    // Operations
    self.addSeat = function() {
        self.cond_report.push(new condition_rows("", self.availableConditions[0]));
    }
    self.removeSeat = function(seat) { self.cond_report.remove(seat) }

    //dependentObservable to represent the last row's value
    self.lastRowValue = ko.dependentObservable(function() {
       var rows = self.cond_report();
       return rows.length ? rows[rows.length - 1].name() : null;
    });

    //subscribe to changes to the last row
    self.lastRowValue.subscribe(function(newValue) {
        if (newValue) {
           self.cond_report.push(new condition_rows('', self));
        }
    });


//var plainJs = ko.toJS(TimeSeqViewModel());
var plainJs = ko.toJS(self.cond_report);
console.log(plainJs)
   // //dependentObservable to represent the last row's value
   // self.panUlRowValue = ko.dependentObservable(function() {
   //    var rows = self.cond_report();
   //    console.log(rows)
   //    return rows.length ? rows[rows.length - 1].name() : null;
   // });


   // //subscribe to changes to the last row
   // self.panUlRowValue.subscribe(function(newValue) {
   //     if (newValue) {
   //        //self.cond_report.push(new condition_rows('', self));
   // //console.log(self.cond_report())
   // //console.log(self.cond_report()[self.each_cond().length - 1])
   // //console.log(self.cond_report()[self.each_cond().length-2].name())
   // draw(self.cond_report()[self.cond_report().length-1].name())
   //     }
   // });


//$('descriptions').focus(function() {
//    console.log('in');
//}).blur(function() {
//    console.log('out');
//    handleClick();

//});


}

ko.applyBindings(new TimeSeqViewModel());


