async function connect(){
    if(global.connection && global.connection.state !== 'disconnected')
        return global.connection;
        
    const mysql = require("mysql2/promise");
    const connection = await mysql.createConnection("mysql://root:root@localhost:3306/painel_digital");
    console.log("Conectou no MySQL!");
    global.connection = connection;
    return connection;
}

async function selectCustomers(){
    const conn = await connect();
    return await conn.query('SELECT * FROM emoji;');
}

module.exports = {selectCustomers}