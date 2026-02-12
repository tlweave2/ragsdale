/**
 * HouseCall Pro Booking Integration - Popup Window Version
 * Opens HouseCall Pro booking in a centered popup window
 */

(function() {
  'use strict';
  
  // HouseCall Pro Configuration
  const HOUSECALLPRO_CONFIG = {
    bookingUrl: 'https://book.housecallpro.com/book/Ragsdales-Heat--Air/024a1eee9a1744658998fb8b5e9b2af5?v2=true&lead_source=website'
  };

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
