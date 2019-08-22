<template>
  <Page class="page" androidStatusBarBackground="#795548">
    <ActionBar title="Manage Items" class="action-bar">
      <NavigationButton text="Go back" android.systemIcon="ic_menu_back" @tap="$navigateBack"/>
    </ActionBar>
    <ItemsList/>
  </Page>
</template>

<script>
import ItemsList from "./ItemsList";

export default {
  components: {
    ItemsList
  }
};
</script>
