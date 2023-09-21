<template>
	<div>
		<section>
			<div class='pic-div'>
			</div>
			<div class="paragragh-div">
 				<h1 class="center heading">Bakery Database</h1>	
				<p>There's a bakery by my house that my family and I go to on a regular basis. 
					I've often wondered how do they know how many items to put out? Why don't they
					try new products? How many products do they role over to the next day? At times 
					my wife and I will discuss these questions and I've told her for a while that I 
					want to build a system that can help a bakery answer some of those questions.
				</p>
				<p>
					This project is designed to be a system that a bakery could use to track the items
					that it has available and to see which items are selling. If they have a certain type
					of donut that is not selling, then why continue to sell that item? That's the main
					purpose and goal of this project.
				</p>
			</div>
		</section>
	</div>
</template>

<script>
export default {
	name: "Top"
}

</script>

<style scoped>

section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  height: 600px;
  margin: 50px 100px 50px 100px;
}

.pic-div {
	display: flex;
  justify-content: center;
  align-items: center;
  background-image: url("../../assets/images/cupcakes.jpg");
  background-position: center;
  background-repeat: no-repeat;
}

.heading {
  text-transform: uppercase;
}

.paragragh-div {
	padding: 50px;
	font-size: 20px;
}

</style>
