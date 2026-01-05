<?php
// Simulazione carico di lavoro (sleep)
usleep(400000+rand(-400000/5, 400000/5));
?>
<!DOCTYPE html>
<html>
<head><title>Servizio: api_v1.php</title></head>
<body>
    <h1>Modulo Dinamico: api_v1.php</h1>
    <p>Elaborazione completata.</p>
    <p>Tempo di esecuzione simulato: 400 ms</p>
    <p>Richiesta processata dal server: <?php echo $_SERVER['SERVER_ADDR']; ?></p>
</body>
</html>
