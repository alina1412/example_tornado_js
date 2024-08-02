'use strict';

let activateSuggest = function () {

  for (let item of ['#1select', '#2select', '#3select'] ) {

    if ($(item).length > 0) { 
      var list = $(item).wrap("<div id='filtersParent' class=\"position-relative\"></div>")
      .select2({
        closeOnSelect: false,
        // maxItems: 7,
        dropdownParent: $(item).parent(),
        escapeMarkup: function(markup) {
          return markup;
        },
        templateResult: function(data) {
          return data.text;
        },
        // templateSelection: function(ar) {
        //   var item = $('<b>' + ar.text + '</b>');
        //   return item;
        // }
        // theme: 'classic'
        // dropdownAdapter: DropdownAdapter
      }).on("select2:closing", function(event) {
        event.preventDefault();
      }).on("select2:closed", function(event) {
        list.select2("open");
      }).on("select2:select", function(event) {
        event.preventDefault();
      }).on('change', function(event) {
        updateFormCnanges(this);
        renewFilters();
      });
      list.select2("open");
      
    }
  }


  // single
  var single = $('#single').wrap("<div id='singleParent' class=\"position-relative\"></div>")
  .select2({
    closeOnSelect: false,
    // maxItems: 1,
    allowClear: true,
    dropdownParent: $('#single').parent(),
    // escapeMarkup: function(markup) {
    //   return markup;
    // },
    // templateResult: function(data) {
    //   return data.text;
    // },
  }).on("select2:closing", function(event) {
    event.preventDefault();
  }).on("select2:closed", function(event) {
    single.select2("open");
  })
  .on("select2:select", function(event) {
    event.preventDefault();
    
    
  })
  .on('change', function(event) {
    event.preventDefault();
    // replaceMulFilterOpt(this);
    console.log('change' + this.value);
  });
  single.select2("open");

}


let getFromForm = function () {
  let formData = $('#myForm').serializeArray();
  let rowsData = { '1select': [], '2select': [], '3select': [], 'single': [] };

  $.each(formData, function (index, field) {
    rowsData[field.name].push(field.value);
  });
  return rowsData
}


let updateFormCnanges = function (opt) {
  // оно думает, что при деселекте вал пустой!!!!!
  console.log(opt.value);
  // console.log();
  let filterId = $(opt).attr('id');
  var newData = [];
  var el = $("#" + filterId);
  el.find('option:selected').each(function() {
    newData.push($(this).val());
  });
  globChoice[filterId] = newData;
  console.log(globChoice);
}


var globChoice = {};
$(document).ready(function () {
  globChoice = getFromForm();
  activateSuggest();

}
);


let renewFilters = function () {
  // selects with multiple choice, renew after each click
  // globChoice = getFromForm();
  let checkData = JSON.stringify(globChoice);
  // console.log(checkData);

  let callUrl = $.post({
    url: '/',
    data: { options: checkData },    // not stringified as a whole, but argument
  });

  callUrl.done(
    function (result) {
      $('#myForm').replaceWith(result);
      activateSuggest();
  })

  return false;
}


let replaceMulFilterOpt = function (btn) {
  let filterId = $(btn).attr('id');
  let newVal = '';
  let wasVal = '';
  $("#single > option").each(function() {
    if ($("#single"+" option[value='"+ this.value  +"']").prop("selected")) {
      wasVal = this.value;
    }
  });
  let lst = $(btn).val();
  // let newLst = [];
  // Removing the specified element by value from the array 
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] === wasVal) {
        let spliced = lst.splice(i, 1);
       
    }
  }


  // let newVal = $("#"+filterId+" option").prop("selected"); //$(btn).val();
  let el = $("#" + filterId);
  globChoice[filterId] = lst;

  // $("#"+filterId+" option").prop("selected", false);
  // $("#"+filterId+" option[value='" + newVal + "']").prop("selected", true);
  // el.val([newVal]).trigger('change');
  renewFilters();
}
