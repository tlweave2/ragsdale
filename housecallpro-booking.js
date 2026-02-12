/**
 * HouseCall Pro Booking Integration
 * Replaces ServiceTitan scheduler with HouseCall Pro booking
 */

(function() {
  'use strict';
  
  // HouseCall Pro Configuration
  const HOUSECALLPRO_CONFIG = {
    bookingUrl: 'https://book.housecallpro.com/book/Ragsdales-Heat--Air/024a1eee9a1744658998fb8b5e9b2af5?v2=true&lead_source=website',
    apiKey: 'REDACTED_API_KEY',
    merchantId: 'c19deeac-7f2b-4782-91be-2cf6a1126647',
    companyId: '024a1eee9a1744658998fb8b5e9b2af5'
  };

  // Create modal HTML
  function createBookingModal() {
    const modalHtml = `
      <div id="hcp-booking-modal" class="hcp-modal" style="display: none;">
        <div class="hcp-modal-overlay"></div>
        <div class="hcp-modal-content">
          <button class="hcp-modal-close" aria-label="Close booking form">&times;</button>
          <iframe 
            id="hcp-booking-iframe" 
            src="${HOUSECALLPRO_CONFIG.bookingUrl}"
            frameborder="0"
            allowfullscreen
            style="width: 100%; height: 100%; border: none;">
          </iframe>
        </div>
      </div>
    `;
    
    document.body.insertAdjacentHTML('beforeend', modalHtml);
    
    // Add CSS styles
    const styles = document.createElement('style');
    styles.textContent = `
      .hcp-modal {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 10000;
      }
      
      .hcp-modal-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.7);
      }
      
      .hcp-modal-content {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 90%;
        max-width: 1000px;
        height: 90%;
        max-height: 800px;
        background: white;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
      }
      
      .hcp-modal-close {
        position: absolute;
        top: 10px;
        right: 10px;
        z-index: 10001;
        width: 40px;
        height: 40px;
        border: none;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 50%;
        cursor: pointer;
        font-size: 24px;
        line-height: 1;
        color: #333;
        transition: all 0.3s ease;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
      }
      
      .hcp-modal-close:hover {
        background: white;
        transform: scale(1.1);
      }
      
      @media (max-width: 768px) {
        .hcp-modal-content {
          width: 95%;
          height: 95%;
          max-width: none;
          max-height: none;
        }
      }
    `;
    document.head.appendChild(styles);
  }

  // Open booking modal
  function openBookingModal() {
    const modal = document.getElementById('hcp-booking-modal');
    if (modal) {
      modal.style.display = 'block';
      document.body.style.overflow = 'hidden';
      
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
    }
  }

  // Close booking modal
  function closeBookingModal() {
    const modal = document.getElementById('hcp-booking-modal');
    if (modal) {
      modal.style.display = 'none';
      document.body.style.overflow = '';
      
      // Track booking closed event
      if (window.digitalData) {
        window.digitalData.push({
          event: 'BookingClosed',
          booking: {
            provider: 'HouseCallPro',
            timestamp: new Date().toISOString()
          }
        });
      }
    }
  }

  // Initialize booking integration
  function initializeBooking() {
    // Create modal once DOM is ready
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', createBookingModal);
    } else {
      createBookingModal();
    }

    // Set up click handlers for all schedule buttons
    document.addEventListener('click', function(e) {
      const scheduleButton = e.target.closest('.schedule-engine-integration-cta');
      if (scheduleButton) {
        e.preventDefault();
        openBookingModal();
      }
    });

    // Close modal handlers
    document.addEventListener('click', function(e) {
      if (e.target.classList.contains('hcp-modal-overlay') || 
          e.target.classList.contains('hcp-modal-close')) {
        closeBookingModal();
      }
    });

    // Close on ESC key
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        closeBookingModal();
      }
    });
  }

  // Start initialization
  initializeBooking();
  
  console.log('HouseCall Pro booking integration loaded');
})();
