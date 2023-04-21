// Функция для автоматического изменения высоты textarea
function autoResizeTextarea() {
  let textareas = document.querySelectorAll(
    'textarea.protocol_fields_title, \
     textarea.protocol_fields_no, \
     textarea.protocol_fields_item, \
     textarea.protocol_fields_responsible, \
     textarea.protocol_fields_deadline, \
     textarea.protocol_fields_status, \
     textarea.protocol_fields_notes, \
     textarea.new-field' // Добавляем новый класс textarea.new-field
  );

  textareas.forEach(textarea => {
    textarea.addEventListener('input', function() {
      this.style.height = 'auto';
      this.style.height = this.scrollHeight + 'px';
    });
  });
}


// Function for cloning table row

document.addEventListener("DOMContentLoaded", function(event) {
  autoResizeTextarea();
  $("#addRowBtn").on("click", function() {
    var $rowTemplate = $("#row-template");
    var $newRow = $rowTemplate.clone(true, true);
    $newRow.find(":input").val("");
    $newRow.removeAttr("id");
    $newRow.appendTo("table");

// Applying styles to textarea in the cloned row
    $newRow.find('textarea').addClass('new-field').css({
      'resize': 'none',
      'outline': 'none',
      'box-sizing': 'border-box',
      'height': '100%'
    });
    autoResizeTextarea(); // Calling the function for automatic resizing of textarea height
  });

// Form handler
  $("#create_protocol_form").on("submit", function() {
    // code
  });
});


