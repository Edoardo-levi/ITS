<?php
// Simulazione carico di lavoro (sleep)
usleep(600000+rand(-600000/5, 600000/5));
?>
<!DOCTYPE html>
<html>
<head><title>Servizio: settings.php</title></head>
<body>
    <h1>Modulo Dinamico: settings.php</h1>
    <p>Elaborazione completata.</p>
    <p>Tempo di esecuzione simulato: 600 ms</p>
    <p>Richiesta processata dal server: <?php echo $_SERVER['SERVER_ADDR']; ?></p>
</body>
</html>
