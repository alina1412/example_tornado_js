'use strict';

let activateSuggest = function () {

  for (let item of ['#1select', '#2select', '#3select'] ) {

    if ($(item).length > 0) { 
      let my_ = $(item).magicSuggest({
        placeholder: 'Select...',
        allowFreeEntries: false,
        cls: 'custom',
        selectionPosition: 'bottom',
        maxSelection: 1, //null,
        selectionStacked: true,
        toggleOnClick: true
      });


      $(my_).on('selectionchange', function (event) { 
        event.preventDefault();
        renewFilters(event);

      });  
    }
  }
}


$(document).ready(function () {
  activateSuggest();

}
);


let renewFilters = function (event) {
  event.preventDefault();
  const formData = $('#myForm').serializeArray();
  let rowsData = { '1select[]': [], '2select[]': [], '3select[]': [] };

  $.each(formData, function (index, field) {
    
    rowsData[field.name].push(field.value);
    
    // else {
    //   rowsData[field.name] = field.value;
    // }
  });


  let checkData = JSON.stringify(rowsData);
  // alert(checkData);
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