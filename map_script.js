// map-interaction.js

// Function to handle the panel toggling
function togglePanel(areaId, panelId) {
    // Show the panel for the clicked area
    document.getElementById(panelId).style.display = 'block';
    
    // Hide all other panels
    let panels = document.querySelectorAll('.info-panel');
    panels.forEach(panel => {
        if (panel.id !== panelId) {
            panel.style.display = 'none';
        }
    });
}

// Event listeners for each area
document.addEventListener('DOMContentLoaded', function () {
    // For Yuki area
    document.getElementById('yuki').addEventListener('click', function() {
        togglePanel('yuki', 'info-panel-yuki');
    });

    // For Akitakada area
    document.getElementById('akitakada').addEventListener('click', function() {
        togglePanel('akitakada', 'info-panel-akitakada');
    });

    document.getElementById('shirokiyama').addEventListener('click', function() {
        togglePanel('shirokiyama', 'info-panel-shirokiyama');
    });
    
    document.getElementById('higashihiroshima').addEventListener('click', function() {
        togglePanel('higashihiroshima', 'info-panel-higashihiroshima');
    });
    
    document.getElementById('takehara').addEventListener('click', function() {
        togglePanel('takehara', 'info-panel-takehara');
    });
    
    document.getElementById('kamikamagari').addEventListener('click', function() {
        togglePanel('kamikamagari', 'info-panel-kamikamagari');
    });
    
    document.getElementById('etajima').addEventListener('click', function() {
        togglePanel('etajima', 'info-panel-etajima');
    });
    
    document.getElementById('kurahashi').addEventListener('click', function() {
        togglePanel('kurahashi', 'info-panel-kurahashi');
    });

    document.getElementById('sera').addEventListener('click', function() {
        togglePanel('sera', 'info-panel-sera');
    });

    document.getElementById('onomichi').addEventListener('click', function() {
        togglePanel('onomichi', 'info-panel-onomichi');
    });

    document.getElementById('fuchu').addEventListener('click', function() {
        togglePanel('fuchu', 'info-panel-fuchu');
    });

    document.getElementById('shobara').addEventListener('click', function() {
        togglePanel('shobara', 'info-panel-shobara');
    });
    
    document.getElementById('shinseki').addEventListener('click', function() {
        togglePanel('shinseki', 'info-panel-shinseki');
    });

    
    // Add more event listeners here for additional areas
});

// Close button functionality
document.addEventListener('DOMContentLoaded', function () {
    
    document.getElementById('close-panel-shirokiyama').addEventListener('click', function() {
        document.getElementById('info-panel-shirokiyama').style.display = 'none';
    });


    // Close panel for Yuki
    document.getElementById('close-panel-yuki').addEventListener('click', function() {
        document.getElementById('info-panel-yuki').style.display = 'none';
    });

    // Close panel for Akitakada
    document.getElementById('close-panel-akitakada').addEventListener('click', function() {
        document.getElementById('info-panel-akitakada').style.display = 'none';
    });
    
    document.getElementById('close-panel-higashihiroshima').addEventListener('click', function() {
        document.getElementById('info-panel-higashihiroshima').style.display = 'none';
    });

    document.getElementById('close-panel-takehara').addEventListener('click', function() {
        document.getElementById('info-panel-takehara').style.display = 'none';
    });

    document.getElementById('close-panel-kamikamagari').addEventListener('click', function() {
        document.getElementById('info-panel-kamikamagari').style.display = 'none';
    });

    document.getElementById('close-panel-etajima').addEventListener('click', function() {
        document.getElementById('info-panel-etajima').style.display = 'none';
    });

    document.getElementById('close-panel-kurahashi').addEventListener('click', function() {
        document.getElementById('info-panel-kurahashi').style.display = 'none';
    });

    document.getElementById('close-panel-sera').addEventListener('click', function() {
        document.getElementById('info-panel-sera').style.display = 'none';
    });

    document.getElementById('close-panel-onomichi').addEventListener('click', function() {
        document.getElementById('info-panel-onomichi').style.display = 'none';
    });

    document.getElementById('close-panel-fuchu').addEventListener('click', function() {
        document.getElementById('info-panel-fuchu').style.display = 'none';
    });
    
    document.getElementById('close-panel-shinseki').addEventListener('click', function() {
        document.getElementById('info-panel-shinseki').style.display = 'none';
    });

    document.getElementById('close-panel-shobara').addEventListener('click', function() {
        document.getElementById('info-panel-shobara').style.display = 'none';
    });


    // Add more close button listeners for additional panels
});

