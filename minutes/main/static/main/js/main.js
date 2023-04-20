
// Function for expanding textarea elements by height as you type, without showing a scrollbar

//document.addEventListener("DOMContentLoaded", function(event) {
//  let textareas = document.querySelectorAll(
//  'textarea.protocol_fields_title, textarea.protocol_fields_no, textarea.protocol_fields_item, textarea.protocol_fields_responsible, textarea.protocol_fields_deadline, textarea.protocol_fields_status, textarea.protocol_fields_notes');
//
//  textareas.forEach(textarea => {
//    textarea.addEventListener('input', function() {
//      this.style.height = 'auto';
//      this.style.height = this.scrollHeight + 'px';
//    });
//  });
//});


document.addEventListener("DOMContentLoaded", function(event) {
  let textareas = document.querySelectorAll(
    'textarea.protocol_fields_title, \
     textarea.protocol_fields_no, \
     textarea.protocol_fields_item, \
     textarea.protocol_fields_responsible, \
     textarea.protocol_fields_deadline, \
     textarea.protocol_fields_status, \
     textarea.protocol_fields_notes'
  );

  textareas.forEach(textarea => {
    textarea.addEventListener('input', function() {
      this.style.height = 'auto';
      this.style.height = this.scrollHeight + 'px';
    });
  });
});

