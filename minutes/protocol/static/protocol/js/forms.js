

$(document).ready(function() {
  var rowCount = 0;

  // Add new fields button
  $("#add-row").click(function() {
    var row = '<div class="form-row">' +
                '<div class="form-group col-md-1">' +
                  '<input type="text" name="no_' + rowCount + '" class="form-control" placeholder="No">' +
                '</div>' +
                '<div class="form-group col-md-4">' +
                  '<input type="text" name="item_' + rowCount + '" class="form-control" placeholder="Item">' +
                '</div>' +
                '<div class="form-group col-md-3">' +
                  '<input type="text" name="responsible_' + rowCount + '" class="form-control" placeholder="Responsible">' +
                '</div>' +
                '<div class="form-group col-md-2">' +
                  '<input type="date" name="deadline_' + rowCount + '" class="form-control" placeholder="Deadline">' +
                '</div>' +
                '<div class="form-group col-md-2">' +
                  '<input type="text" name="status_' + rowCount + '" class="form-control" placeholder="Status">' +
                '</div>' +
              '</div>';
    $('#form-rows').append(row);
    rowCount++;
  });

  // Form submission
  $('#protocol-form').submit(function(event) {
    event.preventDefault();
    var formData = $(this).serialize();

    // Add new fields data
    $('.form-row').each(function(index) {
      var no = $(this).find('input[name^="no"]').val();
      var item = $(this).find('input[name^="item"]').val();
      var responsible = $(this).find('input[name^="responsible"]').val();
      var deadline = $(this).find('input[name^="deadline"]').val();
      var status = $(this).find('input[name^="status"]').val();
      formData += '&no_' + index + '=' + no;
      formData += '&item_' + index + '=' + item;
      formData += '&responsible_' + index + '=' + responsible;
      formData += '&deadline_' + index + '=' + deadline;
      formData += '&status_' + index + '=' + status;
    });

    // Submit
fetch('/submit', {
  method: 'POST',
  body: formData,
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
})
.then(response => {
  if (response.ok) {
    console.log('Form submitted successfully');
  } else {
    console.error('Form submission failed');
  }
})
.catch(error => {
  console.error('Error submitting form:', error);
});
