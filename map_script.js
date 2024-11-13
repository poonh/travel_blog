function togglePanel(areaId, panelId) {
    const panel = document.getElementById(panelId);
    
    // Get the clicked area's position

    const areaElement = document.getElementById(areaId);
    const areaRect = areaElement.getBoundingClientRect();
    
    // Position the panel near the clicked area
    
/*    const clickX = event.clientX - areaRect.left;
    const clickY = event.clientY - areaRect.top;*/
    
    
    const clickX = /*window.scrollX + */window.innerWidth / 2;
    const clickY = window.scrollY /*+ window.innerHeight / 2*/;
    
    panel.style.position = 'absolute';
    panel.style.top = `${clickY + 300}px`/*`${window.scrollY + areaRect.top + areaRect.height}px`*/;
    panel.style.left = `568.5px`/*`${window.scrollX + areaRect.left}px`*/;

    let topValue = panel.style.top;
    console.log(clickX);
    let leftValue = panel.style.left;
    console.log(clickY);
/*    let computedLeftValue = window.getComputedStyle(panel).left;
    console.log("Computed left value:", computedLeftValue)*/
    // Get the click position relative to the image
    /*
    const clickX = event.clientX - areaRect.left;
    const clickY = event.clientY - areaRect.top;

    // Calculate the position to center the panel on the click
    const panelCenterX = clickX - panelElement.offsetWidth / 2;
    const panelCenterY = clickY - panelElement.offsetHeight / 2;

    panel.style.position = 'absolute';
    panel.style.top = `${window.scrollY + areaRect.top + panelCenterY}px`; // Adjust for scroll position and center vertically
    panel.style.left = `${window.scrollX + areaRect.left + panelCenterX}px`; // Adjust for scroll position and center horizontally
    */

    // Show the panel
    panel.style.display = 'block';
    
    // Hide all other panels
    let panels = document.querySelectorAll('.info-panel');
    panels.forEach(p => {
        if (p.id !== panelId) {
            p.style.display = 'none';
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
   

    document.getElementById('unnan').addEventListener('click', function() {
        togglePanel('unnan', 'info-panel-unnan');
    });
    
    document.getElementById('izumo').addEventListener('click', function() {
        togglePanel('izumo', 'info-panel-izumo');
    });
        
    document.getElementById('okuizumo').addEventListener('click', function() {
        togglePanel('okuizumo', 'info-panel-okuizumo');
    });
    
    document.getElementById('ounan').addEventListener('click', function() {
        togglePanel('ounan', 'info-panel-ounan');
    });
    
    document.getElementById('matsue').addEventListener('click', function() {
        togglePanel('matsue', 'info-panel-matsue');
    });
    
    document.getElementById('ota').addEventListener('click', function() {
        togglePanel('ota', 'info-panel-ota');
    });
    
    
    
    // Add more event listeners here for additional areas
/*});

// Close button functionality
document.addEventListener('DOMContentLoaded', function () {*/
    
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
    
    document.getElementById('close-panel-ota').addEventListener('click', function() {
        document.getElementById('info-panel-ota').style.display = 'none';
    });

    document.getElementById('close-panel-matsue').addEventListener('click', function() {
        document.getElementById('info-panel-matsue').style.display = 'none';
    });
    
    document.getElementById('close-panel-unnan').addEventListener('click', function() {
        document.getElementById('info-panel-unnan').style.display = 'none';
    });
    
    document.getElementById('close-panel-izumo').addEventListener('click', function() {
        document.getElementById('info-panel-izumo').style.display = 'none';
    });
    
    document.getElementById('close-panel-okuizumo').addEventListener('click', function() {
        document.getElementById('info-panel-okuizumo').style.display = 'none';
    });
    
    document.getElementById('close-panel-ounan').addEventListener('click', function() {
        document.getElementById('info-panel-ounan').style.display = 'none';
    });

    // Add more close button listeners for additional panels
});

