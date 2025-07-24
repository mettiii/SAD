odoo.define('exam_management.exam_protection', function (require) {
    "use strict";

    var FormController = require('web.FormController');

    FormController.include({
        renderButtons: function () {
            this._super.apply(this, arguments);

            // Disable right-click
            document.addEventListener('contextmenu', event => event.preventDefault());

            // Disable copy/paste/printscreen
            document.addEventListener('keydown', function (e) {
                if (
                    (e.ctrlKey && ['c', 'v', 'x', 'u'].includes(e.key.toLowerCase())) ||
                    e.key === 'PrintScreen' || e.keyCode === 44
                ) {
                    e.preventDefault();
                    alert("Copying or screenshots are not allowed during the exam.");
                }
            });

            // Optional: Add dynamic watermark
            const watermark = document.createElement("div");
            watermark.innerText = "Protected Exam";
            watermark.style = `
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%) rotate(-30deg);
                opacity: 0.1;
                font-size: 50px;
                z-index: 9999;
                pointer-events: none;
            `;
            document.body.appendChild(watermark);
        }
    });
});
