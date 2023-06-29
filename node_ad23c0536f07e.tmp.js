
(async () => {
    const db = require("./db");
    console.log('Começou!');

    console.log('SELECT * FROM EMOJI');
    const clientes = await db.selectCustomers();
    console.log(clientes[0][0]);
})();