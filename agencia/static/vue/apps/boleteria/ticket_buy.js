new Vue({
    el:'#app',
    delimiters: ['{$', '$}'],
    data: {
        list_tickets_buy:[], 
        list_sold_tickets:[],
        route_selected:'',
        show_buy_form:false,
        dni_passenger:'',
        seat_number:''    
    },
    methods:{
        get_list_tickets_buy: function (){
            var self = this;
            axios.get('/box_office/api/ticket/list/buy').then(function (response){
                self.list_tickets_buy = response.data
            })
        },
        get_list_sold_tickets: function (){
            var self = this;
            axios.get('/box_office/api/ticket/list/sold').then(function (response){
                self.list_sold_tickets = response.data
            })
        },
        buy_ticket: function (route_id){
            var self = this;
            self.route_selected = route_id
            self.show_buy_form = true
        },
        pay_ticket:function (ticket_buy_id){
            var self = this;
            var data = {
                'dni_passenger': self.dni_passenger,
                'seat_number': self.seat_number,
                'bus_route':self.route_selected
            }
            axios.post('/box_office/api/ticket/pay', data).then(function (response){
                self.dni_passenger = ''
                self.seat_number = ''
                self.ticket_selected = ''
                self.show_buy_form = false
                self.get_list_sold_tickets()
            })
        }
    },
    beforeMount(){
        this.get_list_tickets_buy(),
        this.get_list_sold_tickets()
     },
});