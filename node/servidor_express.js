const express = require('express');
const { timeStamp } = require('node:console');
const app = express();
const PORT = 4000;

// Middleware para parsear JSON
app.use(express.json());

// Ruta principal
app.get('/', (req, res) => {
    res.json({ 
        mensaje: "Bienvenido a la API principal de Chris", 
        autor: "Chris" });
});

// Ruta de estado
app.get('/estado', (req, res) => {
    res.json({ 
        estado: "Operativo al 100%", 
        framework: "Express.js",
        lenguaje: "JavaScript" 
    });
});

// Ruta POST para recibir y procesar datos enviados por el cliente
app.post('/api/datos', (req, res) => {
    const { usuario, accion } = req.body;

// Validamos que vengan los datos necesarios
    if (!usuario || !accion) {
        return res.status(400).json({
            error: "Faltan datos obligatorios(usuario o accion)."
        });
    }

    res.status(201).json({ 
        mensaje: "Datos procesados con Express correctamente", 
        recibido: {usuario, accion},
        timeStamp: new Date() 
    });
});


// Iniciamos el servidor
app.listen(PORT, () => {
    console.log(`[*] Servidor express corriendo en http://localhost:${PORT}`);
});