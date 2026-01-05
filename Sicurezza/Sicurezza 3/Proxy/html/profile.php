<?php
// Simulazione carico di lavoro (sleep)
usleep(300000+rand(-300000/5, 300000/5));
?>
<!DOCTYPE html>
<html>
<head><title>Servizio: profile.php</title></head>
<body>
    <h1>Modulo Dinamico: profile.php</h1>
    <p>Elaborazione completata.</p>
    <p>Tempo di esecuzione simulato: 300 ms</p>
    <p>Richiesta processata dal server: <?php echo $_SERVER['SERVER_ADDR']; ?></p>
</body>
</html>
