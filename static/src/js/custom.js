odoo.define('academy.custom', function (require) {
"use strict";
console.log("custom js file is loaded successfull")


 var A = require('sum_a');
 var B = require('sum_b');
 
 var C = A + B;
 console.log("value of c:" , C);


/*var core = require('web.core');
var Widget= require('web.Widget');
var basic_fields = require('web.basic_fields');
var fieldRegistry = require('web.field_registry');
var AbstractField = require('web.AbstractField');
var relational_fields = require('web.relational_fields');
var registry = require('web.field_registry');
var special_fields = require('web.special_fields');

*/

/*var CustomFieldIntegerTEST = relational_fields.FieldMany2One.extend({
    init: function () {
     	this._super.apply(this, arguments);
     	
        console.log("this is init function ")
        this.content = 0;
    },
    _onFieldChanged: function (event) {
   
    console.log("this is _onFieldChanged function ")
    
    
  

   
    },

   
  

  
});

fieldRegistry.add('custom_widget', CustomFieldIntegerTEST);*/

});
