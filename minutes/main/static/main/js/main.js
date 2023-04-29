/*  app:  main/static/main.js  */


// Function to close alert messages on 'messaging.html'
function close_alert_fn(){
    const closeButtons = document.querySelectorAll('.close');
    closeButtons.forEach(button => {
        button.addEventListener('click', () => {
            const alertElement = button.parentElement;
            alertElement.remove();
        });
    });
}