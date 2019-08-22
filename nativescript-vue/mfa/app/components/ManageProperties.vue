<template>
  <Page class="page" androidStatusBarBackground="#795548">
    <ActionBar title="Manage Propertys" class="action-bar">
      <NavigationButton text="Go back" android.systemIcon="ic_menu_back" @tap="$navigateBack"/>
    </ActionBar>
    <PropertiesList/>
  </Page>
</template>

<script>
import PropertiesList from "./PropertiesList";

export default {
  components: {
    PropertiesList
  }
};
</script>
