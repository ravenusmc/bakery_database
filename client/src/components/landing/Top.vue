<template>
	<div>
		<section>
			<div class='pic-div'>
			</div>
			<div class="paragragh-div">
 				<h1 class="center heading">Bakery Database</h1>	
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
  margin: 50px 0 50px 0;
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

</style>
