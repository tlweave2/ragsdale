/**
 * HouseCall Pro Booking Integration - Popup Window Version
 * Opens HouseCall Pro booking in a centered popup window
 * 
 * REQUIRES: housecallpro-config.js must be loaded before this script
 */

(function() {
  'use strict';
  
  // Check if config is loaded
  if (!window.HOUSECALLPRO_CONFIG) {
    console.error('HouseCall Pro: Configuration not loaded. Make sure housecallpro-config.js is included before this script.');
    return;
  }
  
  const HOUSECALLPRO_CONFIG = window.HOUSECALLPRO_CONFIG;

  // Open booking in centered popup window
  function openBookingPopup() {
    const width = 1000;
    const height = 800;
    const left = (screen.width - width) / 2;
    const top = (screen.height - height) / 2;
    
    const popup = window.open(
      HOUSECALLPRO_CONFIG.bookingUrl,
      'HouseCallProBooking',
      `width=${width},height=${height},left=${left},top=${top},resizable=yes,scrollbars=yes,status=yes`
    );
    
    if (popup) {
      popup.focus();
      
      // Track booking opened event
      if (window.digitalData) {
        window.digitalData.push({
          event: 'BookingStarted',
          booking: {
            provider: 'HouseCallPro',
            timestamp: new Date().toISOString()
          }
        });
      }
    } else {
      // Popup blocked - open in new tab as fallback
      window.open(HOUSECALLPRO_CONFIG.bookingUrl, '_blank');
    }
  }

  // Set up click handlers for all schedule buttons
  document.addEventListener('click', function(e) {
    const scheduleButton = e.target.closest('.schedule-engine-integration-cta');
    if (scheduleButton) {
      e.preventDefault();
      openBookingPopup();
    }
  });
  
  console.log('HouseCall Pro booking integration loaded (Popup version)');
})();
