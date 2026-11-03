const http = require('http');
const PORT = 4000;

const server = http.createServer((req, res) => {
    // Evaluamos qué ruta está pidiendo el usuario (req.url)
    if (req.url === '/') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ mensaje: "Bienvenido a la API principal de Chris", ruta: "Inicio" }));
    
    } else if (req.url === '/estado') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ estado: "Sistema funcionando al 100%", servidor: "Node.js Activo" }));
    
    } else {
        // Si la ruta no existe, devolvemos un error 404
        res.writeHead(404, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: "Ruta no encontrada", codigo: 404 }));
    }
});

server.listen(PORT, () => {
    console.log(`[*] Servidor con rutas corriendo en http://localhost:${PORT}`);
});