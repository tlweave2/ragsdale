/**
 * HouseCall Pro Booking Integration
 * Replaces ServiceTitan scheduler with HouseCall Pro booking
 * 
 * NOTE: This is the iframe/modal version (not currently used)
 * The simpler popup version (housecallpro-booking-simple.js) is being used instead
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

  // Create modal HTML
  function createBookingModal() {
    const modalHtml = `
      <div id="hcp-booking-modal" class="hcp-modal" style="display: none;">
        <div class="hcp-modal-overlay"></div>
        <div class="hcp-modal-content">
          <button class="hcp-modal-close" aria-label="Close booking form">&times;</button>
          <div id="hcp-loading" class="hcp-loading">
            <div class="hcp-spinner"></div>
            <p>Loading booking form...</p>
          </div>
          <iframe 
            id="hcp-booking-iframe" 
            src=""
            frameborder="0"
            allowfullscreen
            allow="payment"
            style="width: 100%; height: 100%; border: none; background: white;">
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
      
      .hcp-loading {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        z-index: 1;
      }
      
      .hcp-spinner {
        border: 4px solid #f3f3f3;
        border-top: 4px solid #e74c3c;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        animation: hcp-spin 1s linear infinite;
        margin: 0 auto 20px;
      }
      
      @keyframes hcp-spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
      }
      
      .hcp-loading p {
        color: #333;
        font-size: 16px;
        margin: 0;
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
    const iframe = document.getElementById('hcp-booking-iframe');
    const loading = document.getElementById('hcp-loading');
    
    if (modal && iframe) {
      // Show loading indicator
      if (loading) {
        loading.style.display = 'block';
      }
      
      // Set iframe src to trigger loading
      if (!iframe.src) {
        iframe.src = HOUSECALLPRO_CONFIG.bookingUrl;
        
        console.log('HouseCall Pro: Loading booking form...', HOUSECALLPRO_CONFIG.bookingUrl);
        
        // Hide loading when iframe loads
        iframe.onload = function() {
          console.log('HouseCall Pro: Iframe loaded');
          if (loading) {
            loading.style.display = 'none';
          }
        };
        
        // Detect if iframe is blocked
        iframe.onerror = function() {
          console.log('HouseCall Pro: Iframe blocked, opening in new window');
          closeBookingModal();
          window.open(HOUSECALLPRO_CONFIG.bookingUrl, '_blank', 'width=1000,height=800');
        };
        
        // Check after timeout if iframe loaded
        setTimeout(function() {
          if (loading && loading.style.display !== 'none') {
            console.log('HouseCall Pro: Iframe may be blocked, showing fallback');
            if (loading) {
              loading.innerHTML = '<div class="hcp-spinner"></div><p>Having trouble loading?</p><button id="hcp-open-new-window" style="margin-top: 15px; padding: 10px 20px; background: #e74c3c; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px;">Open in New Window</button>';
              
              document.getElementById('hcp-open-new-window').onclick = function() {
                closeBookingModal();
                window.open(HOUSECALLPRO_CONFIG.bookingUrl, '_blank', 'width=1000,height=800');
              };
            }
          }
        }, 3000);
      }
      
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
