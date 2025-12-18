<?php
// Simulazione carico di lavoro (sleep)
usleep(2000000+rand(-2000000/5, 2000000/5));
?>
<!DOCTYPE html>
<html>
<head><title>Servizio: upload.php</title></head>
<body>
    <h1>Modulo Dinamico: upload.php</h1>
    <p>Elaborazione completata.</p>
    <p>Tempo di esecuzione simulato: 2000 ms</p>
    <p>Richiesta processata dal server: <?php echo $_SERVER['SERVER_ADDR']; ?></p>
</body>
</html>
