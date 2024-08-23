'use strict';

var globChoice = {};
$(document).ready(function () {
  globChoice = getFromForm();
  activateSuggest();


});


let showAlwaysOpen = function () {
  $('body').on('click', function(event){
    event.stopPropagation();
    $("#4select").trigger('chosen:open');
  });
}


let activateSuggest = function () {
  let search_exist = true;

  for (let item of ['#1select', '#2select', '#3select', '#4select'] ) {

    if ($(item).length > 0) { 
      $(item).chosen({ 
        width:'100%',
        disable_search: search_exist,
        inherit_select_classes: true,
        no_results_text: 'Нет совпадений'
      });
    }
  }
  // renewFilters();
}

let renewFilters = function () {
  // selects with multiple choice, renew after each click
  globChoice = getFromForm();
  let checkData = JSON.stringify(globChoice);
  console.log(checkData);

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

let unselectFromFilterOpts = function (btn) {
  let filterId = $(btn).parent().attr('data-name');
  let deleteVal = $(btn).attr('data-val');
  let el = $("#" + filterId);
  let newData = [];
  //TODO
  console.log(filterId)
  renewFilters();

}




let getFromForm = function () {
  let formData = $('#myForm').serializeArray();
  let rowsData = { '1select': [], '2select': [], '3select': [], 'single': [], '4select': [] };

  $.each(formData, function (index, field) {
    rowsData[field.name].push(field.value);
  });
  return rowsData
}

