from selenium.webdriver.common.by import By
#以下服务器域名地址
url = "https://passport-fat.e-ports.com/"
#密码登录
login_change_password=By.CSS_SELECTOR,'div.ant-spin-nested-loading div.ant-spin-container div.index_box_2UojT div.index_container_1MNkV div.index_container_right_3Bvs9 div.index_loginWayTabs_1VLgK div.index_loginWayTab_4izMu:nth-child(2) > button.ant-btn.ant-btn-block'
#邮箱登录
login_change_mail=By.CSS_SELECTOR, '#rc-tabs-0-tab-2'
#邮箱账号
login_input_mail=By.CSS_SELECTOR, '#basic_username'
#密码
login_input_password=By.CSS_SELECTOR, '#password'
#点击登录按钮
login_click_login_button=By.CSS_SELECTOR,'div.ant-spin-nested-loading div.ant-spin-container div.index_box_2UojT div.index_container_1MNkV div.index_container_right_3Bvs9 div.index_control_1nH9j form.ant-form.ant-form-horizontal div.index_submitBtn_3uYl6:nth-child(5) > button.ant-btn.ant-btn-lg.ant-btn-block'
#用户昵称
login_nickname=By.CSS_SELECTOR,'div.header___2Uhn5:nth-child(1) div.headerInfo___3H6YW div.userWrapper___1KWhJ div.ant-dropdown-trigger.avatarContianer___1_ljY div.avatarName___27ptB > span.name___IW1ZM'
#退出登录
login_logout=By.CSS_SELECTOR,'div.header___2Uhn5:nth-child(1) div.headerInfo___3H6YW div.userWrapper___1KWhJ div.ant-dropdown.ant-dropdown-placement-bottomRight ul.ant-dropdown-menu.ant-dropdown-menu-root.ant-dropdown-menu-vertical.ant-dropdown-menu-light:nth-child(1) li.ant-dropdown-menu-item.ant-dropdown-menu-item-only-child:nth-child(3) span.ant-dropdown-menu-title-content > div:nth-child(1)'
#确定退出登录
login_logout_bt=By.CSS_SELECTOR,'div.ant-modal-root div.ant-modal-wrap div.ant-modal div.ant-modal-content:nth-child(2) div.ant-modal-footer > button.ant-btn.ant-btn-primary:nth-child(2)'

#发布询价page_inquery
#订单管理按钮
order_manager_list = By.CSS_SELECTOR,'div.header___2Uhn5:nth-child(1) div.topMenu___11GKd ul.ant-menu-overflow.ant-menu.ant-menu-root.ant-menu-horizontal.ant-menu-dark:nth-child(1) li.ant-menu-overflow-item.ant-menu-item.ant-menu-item-only-child:nth-child(3) > span.ant-menu-title-content'
#发布询价按钮
add_inquery = By.CSS_SELECTOR,'div.qiankun-micro-app div.qiankun-micro-app-container div.router-wrapper div.main-wrapper section.ant-layout section.ant-layout main.container.ant-layout-content div.ant-spin-nested-loading div.ant-spin-container div.src-layouts-PageLayout-index-module__pageLayout--2dT3G.src-pages-orderNew-index-module__orderList--2P0ZN div.src-layouts-PageLayout-index-module__pageHeader--fwpFW div.src-layouts-PageLayout-index-module__heading--2IRYx:nth-child(1) div.src-layouts-PageLayout-index-module__extra--3qdgQ > button.ant-btn.ant-btn-primary'
