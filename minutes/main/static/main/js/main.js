/*  app:  main/static/main.js  */


// function for closing alert shields at 'messaging.html'
function close_alert_fn(){
    const closeButtons = document.querySelectorAll('.close');
    closeButtons.forEach(button => {
        button.addEventListener('click', () => {
            const alertElement = button.parentElement;
            alertElement.remove();
        });
    });
}