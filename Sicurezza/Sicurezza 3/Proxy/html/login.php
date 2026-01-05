<?php
// Simulazione carico di lavoro (sleep)
usleep(200000+rand(-200000/5, 200000/5));
?>
<!DOCTYPE html>
<html>
<head><title>Servizio: login.php</title></head>
<body>
    <h1>Modulo Dinamico: login.php</h1>
    <p>Elaborazione completata.</p>
    <p>Tempo di esecuzione simulato: 200 ms</p>
    <p>Richiesta processata dal server: <?php echo $_SERVER['SERVER_ADDR']; ?></p>
</body>
</html>
