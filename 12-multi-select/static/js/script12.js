$(document).ready(function () {
  $('#my_select').magicSuggest({
    placeholder: 'Select...',
    allowFreeEntries: false,
    cls: 'custom',
    selectionPosition: 'bottom',
    maxSelection: null,
    selectionStacked: true,
    toggleOnClick: true
  });
});


let getFromForm = function (event) {
  event.preventDefault();
  const formData = $('#myForm').serializeArray();
  let rowsData = { 'mul_select[]': [] };

  $.each(formData, function (index, field) {
    if (field.name == 'mul_select[]') {
      rowsData['mul_select[]'].push(field.value);
    }
    else {
      rowsData[field.name] = field.value;
    }
  });

  // for every field of checkbox just to be there
  // $('input[type="checkbox"]').each(function(){
  //   rowsData[this.name] = false;
  // })

  // // only if true - rewrite (because there's 2 checkboxes - one on top of another)
  // $('input[type="checkbox"]').each(function(){
  //   if ($(this).prop('checked') == true) {
  //     rowsData[this.name] = true;
  //   }
  // });

  let checkData = JSON.stringify(rowsData);
  alert(checkData);
  console.log(checkData);
  return false;
}