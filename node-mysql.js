const mysql= require("mysql2/promise");

async function connectToMySQL(){
    //Establish a database connection
    const con = await mysql.createConnection({
        user:"root",
        password:"password",
        host:"localhost",
        database: "mydb"
    });
    console.log("Successfully connected!");
    //Run SQL queries

    //Insert data
    /*
    let [results] = await con.execute("INSERT INTO product(name) VALUES('BOBA')");
    console.log(results);
    */

    //Delete data
    /*
    let [results] = await con.execute("DELETE FROM product WHERE id=8"); 
    console.log(results);
    */

    //Update data
    /*
    let [results] = await con.execute("UPDATE product SET name='AMERICANO COFFEE' WHERE id=1"); 
    console.log(results);
    */

    //Setup variables
    /*
    let newName="AMERICANO"; 
    let productID=1; 
    let [results] = await con.execute("UPDATE product SET name=? WHERE id=?", [newName,productID]); 
    console.log(results);
    */

    //Fetch data
    /*
    let [results] = await con.execute("SELECT * FROM product");
    results.forEach(product => {
        console.log(product.name);
    });
    */
   
    //Close the connection
    con.end(); 
}

connectToMySQL(); 