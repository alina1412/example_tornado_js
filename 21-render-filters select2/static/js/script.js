'use strict';

let activateSuggest = function () {

  for (let item of ['#1select', '#2select', '#3select'] ) {

    if ($(item).length > 0) { 
      var list = $(item).wrap("<div id='filtersParent' class=\"position-relative\"></div>")
      .select2({
        closeOnSelect: false,
        maxItems: 7,
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
        // console.log(this.value);
        // console.log($(this).attr('id'));
        // renewFilters();
      }).on('change', function(event) {
        // console.log(this.value);
        // console.log($(this).attr('id'));
        // $('.form-control').prop("disabled", true);
        updateFormCnanges(this);
        renewFilters();
      });
      list.select2("open");
      
    }
  }
}


let getFromForm = function () {
  let formData = $('#myForm').serializeArray();
  let rowsData = { '1select': [], '2select': [], '3select': [] };

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
  let rowsData = getFromForm();
  let checkData = JSON.stringify(rowsData);
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