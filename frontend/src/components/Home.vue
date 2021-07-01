<template>
  <div class='overflow-hidden'>
    <div class="home container">
      <div class="row">
        <div class="col-lg-6 col-md-9 col-sm-12">
          <div class="">
            <h1 class='top-text'>Fundraising for the people and causes you care about.</h1>
            <h4 class='mid-text mt-4 mb-4'>Get Started Today.</h4>
            <a class='d-flex justify-content-start btn btn-lg btn-success my-btn text-light' href='#'>Start a Fundraiser</a>
          </div>
        </div>
        <div class="col-lg-6 col-md-3 d-none d-lg-block d-md-block">
          <img :src="require(`@/assets/5240.jpg`)" class='img img-fluid myimg'>
        </div>
      </div>
    </div> 
    <div class="carousel-section container">
      <carousel :items-to-show="2" :wrap-around='true'>
        <Slide v-for="image in images" :key="image">
          <img :src=image.link class='img img-fluid slider-img'>
          <p class='text-muted mt-4 img-text'>{{image.text}}</p>
        </Slide>

        <template #addons>
          <Navigation />
        </template>
      </carousel>
    </div>
    <div class="featured-section">
      <div class="container">
        <h3 class='text-success'>Popular Fundraisers</h3> 
        <div class="fundraisers mt-4 container">
          <div class="row">
            <div v-for="campaign in popular" :key="campaign" class="col-lg-3 col-sm-6 campaign justify-content-center">
                <img :src=campaign.media class='img img-fluid campaign-image'>
                <div class='categories'>
                  <span v-for="category in campaign.categories" :key="category" class='category'>{{category}}</span>
                </div>
                <h4 class='text-muted align-left campaign-title'>{{campaign.title}}</h4>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import 'vue3-carousel/dist/carousel.css';
import { Carousel, Slide, Navigation } from 'vue3-carousel';

export default {
  name: 'Home',
  components: {
    Carousel,
    Slide,
    Navigation,
  },
  data(){
    return {
      images:[
        {'link': require(`@/assets/1.png`),'text':'Over 4000 Nigerian kids are not in school, start a fundraising campaign.'},
        {'link': require(`@/assets/2.png`),'text':'Fundraise to provide food and shelter for the homeless and needy.'},
        {'link': require(`@/assets/3.jpg`),'text':'You have plans to study abroad? Open a fundraiser and share to your friends.'},
        {'link': require(`@/assets/4.jpg`),'text':'Start a campaign to raise money for yourself and others during this lockdown.'},
        {'link': require(`@/assets/5.jpg`),'text':'Help a friend raise money for surgery or medication'}
      ],
      popular: [
        {'media': require(`@/assets/1.png`), 'title': "Ifunaya's Heart Transplant", 'categories': ['Health','Emergency'],'percentage': 30, 'amount_raised': 200000, 'deadline': '3 days left'},
        {'media': require(`@/assets/4.jpg`), 'title': "Let's get Ayo to Harvard Business School", 'categories': ['Education'],'percentage': 60, 'amount_raised': 1360000, 'deadline': '1 month left'},
        {'media': require(`@/assets/2.png`), 'title': "Operation Send 100 Kogi Kids to School", 'categories': ['Education','Charity'],'percentage': 70, 'amount_raised': 105750, 'deadline': '2 weeks left'},
        {'media': require(`@/assets/5.jpg`), 'title': "Help Jay get a laptop to code", 'categories': ['Tech','Education'],'percentage': 15, 'amount_raised': 12050, 'deadline': '2 months left'}
      ]
    }
  }
  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.row {
    display: flex;
    justify-content: space-around;
    align-items: center;
    flex-wrap: wrap;
}


.mid-text,
.top-text{
  text-align: left;
}

.top-text{
  font-display: bold;
  font-weight: 600;
  font-size: 40px;
  color: #3A3838;
}

.mid-text{
  font-weight: 400;
  font-size: 30px;
  color: #3A3838;
}

.my-btn{
  width: 220px;
  padding: 7px 20px;
  margin-top: 45px;
}

.home{
  padding: 100px 20px;
}

.myimg{
  max-height: 100%;

}

.featured-section{
  padding: 30px 0px 50px 0px;
  background: rgb(213, 245, 213);
}

.carousel-section{
  padding: 100px 0px;
}

.slider-img{
  min-height: 150px;
  max-height: 300px;
  border-radius: 15px;
}

.fundraisers{
  padding: 30px 0px;
}

.campaign{
  height: 400px;
}

.campaign-title{
  text-align: left;
  margin-top: 10px;
}

.campaign-image{
  height: 200px;
}

.categories{
  margin-top: 10px;
  text-align: left;
}

.category{
  margin: 0px 4px 0px 0px;
  padding: 6px 9px;
  border-radius: 2px;
  font-size: 10px;
  background: green;
  color: #ffffff;
  cursor: pointer;
  transition: 0.2s ease-in;
}

.category:hover{
  transition: 0.2s ease-out;
}


@media screen and (max-width: 450px) {
  .carousel__prev,
  .carousel__next{
    margin: 100px;
  }

  .img-text{
    font-size: 10px;
  }
}

</style>
