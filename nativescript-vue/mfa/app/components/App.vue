<template>
  <Page class="page" androidStatusBarBackground="#795548">
    <ActionBar :title="selectedTable ? selectedTable : 'Tables'" class="action-bar">
      <NavigationButton
        v-show="selectedTable"
        text="Menu"
        android.systemIcon="ic_menu_more"
        @tap="openDrawer()"
      />
    </ActionBar>
    <RadSideDrawer ref="drawer">
      <StackLayout ~drawerContent class="sideStackLayout">
        <StackLayout class="sideTitleStackLayout"></StackLayout>
        <StackLayout class="sideStackLayout">
          <Label text="Tables" class="sideLabel" @tap="showHomePage()"/>
          <Label
            v-if="selectedTable != ''"
            text="Items"
            class="sideLabel"
            @tap="navigateToItems()"
          />
          <Label
            v-if="selectedTable != ''"
            text="Properties"
            class="sideLabel"
            @tap="navigateToProperties()"
          />
        </StackLayout>
      </StackLayout>
      <StackLayout ~mainContent>
        <AbsoluteLayout>
          <template v-if="selectedTable == ''">
            <ListView for="table in tables" height="100%" width="100%">
              <v-template>
                <GridLayout columns="*,25" rows="*">
                  <Label
                    col="0"
                    :text="table"
                    class="m-5"
                    @tap="selectTable(table)"
                    textWrap="true"
                    fontSize="18"
                  />
                  <Label
                    col="1"
                    :text="String.fromCharCode(0xe9ad)"
                    class="icon p-t-5 p-r-5"
                    @tap="confirmDelete(table)"
                  />
                </GridLayout>
              </v-template>
            </ListView>
            <AbsoluteLayout marginTop="90%" marginLeft="85%">
              <AddButton @onButtonTap="selectTable()"/>
            </AbsoluteLayout>
          </template>
          <Table v-else/>
        </AbsoluteLayout>
      </StackLayout>
    </RadSideDrawer>
  </Page>
</template>

<script>
import AddButton from "./AddButton";
import EditModal from "./EditModal";
import ManageItems from "./ManageItems";
import ManageProperties from "./ManageProperties";
import Table from "./Table";
import { mapActions, mapGetters } from "vuex";
var dialogs = require("tns-core-modules/ui/dialogs");

export default {
  created() {
    this.initTables();
  },
  components: {
    AddButton,
    Table
  },
  data() {
    return {};
  },
  methods: {
    ...mapActions([
      "initTables",
      "initTable",
      "deleteTable",
      "setItemsSetupDone",
      "setPropertiesSetupDone",
      "setSelectTable"
    ]),
    openDrawer() {
      this.$refs.drawer.nativeView.showDrawer();
    },
    onCloseDrawerTap() {
      this.$refs.drawer.nativeView.closeDrawer();
    },
    navigateToItems() {
      this.$navigateTo(ManageItems);
    },
    navigateToProperties() {
      this.$navigateTo(ManageProperties);
    },
    selectTable(table) {
      if (table) {
        this.initTable(table);
      } else {
        this.$showModal(EditModal, {
          props: {
            addNew: true,
            labelData: {}
          }
        });
      }
    },
    showHomePage() {
      this.initTables().then(() => {
        this.setSelectTable("");
        this.onCloseDrawerTap();
      });
    },
    confirmDelete(table) {
      confirm({
        title: "Delete",
        message: "Are you sure you want to delete " + table + " ?",
        okButtonText: "Delete",
        cancelButtonText: "Cancel"
      }).then(result => {
        if (result) {
          this.deleteTable(table);
        }
      });
    }
  },
  computed: {
    ...mapGetters({
      selectedTable: "table",
      tables: "tables"
    })
  }
};
</script>

<style>
.page {
  color: black;
  background-image: url("~/assets/images/Background.jpeg");
  background-size: cover;
}
.sideStackLayout {
  background: #795548;
  color: white;
  width: 180;
  font-size: 18;
}
.sideLabel {
  font-size: 20;
  padding: 5 10;
}
.link {
  color: blue;
}
.icon {
  font-family: "icomoon";
  font-size: 20;
  color: lightslategray;
}
ListView {
  background-color: transparent;
}
Button {
  color: white;
  background-color: #487955;
  margin: 5;
  border-radius: 20%;
}
</style>
