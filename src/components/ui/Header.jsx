import React from 'react';
import { Bell, LogOut, X } from 'lucide-react';

// Custom Fundile Logo Component
const FundileLogo = ({ className = "h-48 w-48" }) => (
  <svg 
    xmlns="http://www.w3.org/2000/svg" 
    className={className}
    viewBox="0 0 2200 800" 
    style={{ fontFamily: 'Afacad, sans-serif' }}
  >
    <defs>
      <style type="text/css">
        @import url('https://fonts.googleapis.com/css2?family=Afacad:wght@700&amp;display=swap');
      </style>
    </defs>

    <g transform="translate(23, -76)">
      <g>
        <g transform="translate(150, 101.77) scale(0.75)">
          <path transform="translate(-166.4869, -27.606)" fill="#ff9100" opacity="1.000000" stroke="none" d="M281.100800,82.430374 C296.863281,82.430435 312.139648,82.430435 327.589142,82.430435 &#10;&#10;      C327.589142,101.156349 327.589142,119.218277 327.589142,137.604797 &#10;&#10;      C309.226532,137.604797 291.146423,137.604797 272.610504,137.604797 &#10;&#10;      C272.610504,119.531845 272.610504,101.481499 272.610504,82.430305 &#10;&#10;      C275.160431,82.430305 277.887573,82.430305 281.100800,82.430374 z"/>
          <path fill="#ff9100" opacity="1.000000" stroke="none" d="M281.100800,82.430374 C296.863281,82.430435 312.139648,82.430435 327.589142,82.430435 &#10;&#10;      C327.589142,101.156349 327.589142,119.218277 327.589142,137.604797 &#10;&#10;      C309.226532,137.604797 291.146423,137.604797 272.610504,137.604797 &#10;&#10;      C272.610504,119.531845 272.610504,101.481499 272.610504,82.430305 &#10;&#10;      C275.160431,82.430305 277.887573,82.430305 281.100800,82.430374 z"/>
          <path fill="#ff9100" opacity="1.000000" stroke="none" d="M234.051895,135.066223 &#10;&#10;      C224.745880,148.067596 215.644699,160.771545 206.224594,173.920700 &#10;&#10;      C191.142197,163.057236 176.346191,152.400055 161.102249,141.420258 &#10;&#10;      C171.897430,126.295197 182.400925,111.578819 193.222076,96.417397 &#10;&#10;      C208.472687,107.127121 223.382523,117.597542 238.759613,128.396088 &#10;&#10;      C237.075623,130.779358 235.666183,132.774078 234.051895,135.066223 z"/>
          <path fill="#ff9100" opacity="1.000000" stroke="none" d="M287.318604,233.165192 &#10;&#10;      C273.012787,244.051132 258.971313,254.686829 244.461060,265.677582 &#10;&#10;      C233.276215,250.872467 222.308655,236.354980 211.026871,221.421555 &#10;&#10;      C225.902328,210.163956 240.315781,199.255997 254.990143,188.150589 &#10;&#10;      C256.061981,189.313354 257.003143,190.179214 257.763031,191.182358 &#10;&#10;      C267.103516,203.512344 276.449860,215.838257 285.690308,228.242981 &#10;&#10;      C286.661530,229.546768 286.967987,231.345734 287.318604,233.165192 z"/>
        </g>
        <path fill="#ff9100" opacity="1.000000" stroke="none" d=" M346.618164,323.599243   C390.887054,300.100555 434.830627,276.778168 478.816315,253.535477   C490.312988,247.460464 502.069885,242.258408 515.593506,242.888382   C526.837036,243.412109 536.962891,247.456100 546.631958,252.590546   C605.086304,283.631073 663.469849,314.805176 721.830627,346.021515   C741.277954,356.423615 760.671387,366.933228 779.924744,377.688446   C788.846985,382.672546 793.581482,390.354065 793.151917,401.025787   C792.944519,406.178833 790.979065,410.274750 786.950012,412.873901   C776.925781,419.340515 766.795715,425.687531 756.382141,431.498291   C715.830627,454.125977 675.130371,476.487030 634.528320,499.024323   C603.924683,516.011719 573.575562,533.471863 542.694214,549.935608   C534.276367,554.423462 524.518555,557.463745 515.060120,558.648132   C504.622375,559.955017 494.436676,555.726318 485.240387,550.665100   C439.169922,525.310059 393.255981,499.670929 347.238922,474.218567   C315.021484,456.398865 282.718964,438.733063 250.479980,420.952118   C247.576355,419.350677 244.919174,417.307678 242.047882,415.641510   C228.019974,407.501282 231.543488,389.717133 240.164764,382.425934   C245.302017,378.081238 251.256653,374.559265 257.211456,371.349426   C286.843445,355.376984 316.597473,339.630981 346.618164,323.599243  M509.620361,444.230133   C512.299622,444.117645 515.457214,444.896881 517.584778,443.755798   C540.802307,431.303711 563.873291,418.577637 586.946411,405.857727   C591.374939,403.416290 591.300964,401.418671 586.821289,398.972992   C563.992676,386.509277 541.118408,374.128845 518.327942,361.595978   C514.570251,359.529572 511.388153,359.634857 507.630035,361.713196   C485.298676,374.062622 462.845703,386.191986 440.495819,398.508331   C438.778381,399.454742 437.540466,401.126362 436.079681,402.538502   C437.656189,403.882191 439.057922,405.543751 440.835754,406.511321   C463.496643,418.986617 486.211426,431.348831 509.620361,444.085133  z"/>
        <path fill="#ff9100" opacity="1.000000" stroke="none" d=" M530.902283,583.963318   C579.000061,555.740784 626.738159,527.630981 675.098083,499.154999   C675.098083,501.254150 675.080383,502.833069 675.100769,504.411560   C675.431519,530.050720 676.440857,555.704041 675.899902,581.324646   C675.419739,604.060913 666.363403,623.657898 648.652710,638.331360   C640.255859,645.288208 630.888550,651.135437 621.655457,657.004822   C611.017029,663.767578 600.027039,669.975891 589.215393,676.467773   C573.771118,685.741272 558.458008,695.238708 542.890686,704.299988   C525.288452,714.545654 506.851746,716.305420 488.165741,707.565125   C473.860107,700.873718 459.910980,693.423096 445.759888,686.397583   C421.355072,674.281494 396.832611,662.399475 372.516479,650.108765   C349.411194,638.429932 333.341370,620.744141 327.668762,594.873291   C326.400208,589.087646 325.419006,583.097412 325.412933,577.200256   C325.381042,546.214417 325.703827,515.228271 325.917938,484.242279   C325.919891,483.960632 326.119965,483.680389 326.393372,482.966705   C337.198914,489.207153 347.928986,495.411743 358.666290,501.603729   C406.111877,528.964600 453.515015,556.399719 501.075989,583.558533   C505.773682,586.241089 511.401672,588.452820 516.671387,588.624268   C521.240967,588.773010 525.914856,585.716187 530.902283,583.963318  z"/>
        <path fill="#ff9100" opacity="1.000000" stroke="none" d=" M727.104553,542.000000 C727.104492,554.662109 727.255981,566.827271 727.010742,578.984436 C726.939697,582.507202 727.955078,584.633972 730.756042,586.836365 C745.057800,598.081787 747.519531,617.167419 735.435364,629.111267 C730.770569,633.721924 731.136902,637.142212 732.927734,642.274536 C738.051880,656.959961 742.820801,671.769775 747.685852,686.545044 C751.600159,698.432983 748.005920,705.663330 735.837463,709.084167 C723.171570,712.644958 710.215027,711.725037 697.413269,709.852844 C692.003113,709.061584 687.834473,705.635925 684.933289,700.724121 C682.407043,696.447144 682.672607,692.277222 684.186523,687.836975 C689.837402,671.263672 695.343201,654.640625 701.083069,638.098511 C702.138062,635.057983 701.908508,633.276367 699.294861,630.955688 C686.045898,619.191650 687.093201,598.850830 701.525269,587.564697 C704.625305,585.140381 705.654602,582.683167 705.627808,578.857422 C705.446960,553.035034 705.451660,527.210693 705.563782,501.387695   C705.577026,498.349792 706.090027,495.091919 707.283569,492.330231   C709.385864,487.465454 715.054260,484.735840 719.237549,485.864258   C724.024475,487.155518 727.051208,491.551239 727.070496,497.516357   C727.117920,512.177490 727.097900,526.838745 727.104553,542.000000 z"/>
      </g>
      <text x="850" y="243" dominantBaseline="hanging" fontFamily="Afacad, sans-serif" fill="white" fontSize="466" fontWeight="700">fundile</text>
    </g>
  </svg>
);

const formatNotificationDate = (value) => {
  if (!value) {
    return 'Just now';
  }

  const dateValue = value?.toDate ? value.toDate() : new Date(value);
  if (Number.isNaN(dateValue.getTime())) {
    return 'Just now';
  }

  return dateValue.toLocaleDateString(undefined, { month: 'short', day: 'numeric' });
};

const Header = ({ currentUser, onLogout, onMarkAllNotificationsRead, onMarkNotificationRead, pendingAssignments, studentNotifications = [], superAdminMode, setSuperAdminMode, superAdminTier, setSuperAdminTier, brandPalette, setBrandPalette }) => {
  const [showNotifications, setShowNotifications] = React.useState(false);
  const [showLogoutConfirm, setShowLogoutConfirm] = React.useState(false);
  const unreadNotificationCount = studentNotifications.filter((notification) => !notification.isRead).length;
  const systemNoticeCount = pendingAssignments.length > 0 ? 1 : 0;
  const unreadCount = unreadNotificationCount + systemNoticeCount;

  return (
    <header className="bg-[#13519C] shadow-sm sticky top-0 z-30">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <div className="flex items-center space-x-3 shrink-0">
            <FundileLogo className="h-28 w-28 sm:h-48 sm:w-48" />
          </div>
          
          {currentUser && (
            <div className="flex items-center space-x-4">
              <span className="text-white font-medium hidden sm:inline" style={{ fontFamily: 'Afacad, sans-serif' }}>
                Welcome, {currentUser.name} ({currentUser.role})
              </span>

              {currentUser.isSuperAdmin && (
                <div className="flex flex-col sm:flex-row items-end sm:items-center gap-1 sm:gap-2 lg:gap-3 justify-end flex-1 min-w-0">
                  <div className="flex flex-wrap items-center gap-1 sm:space-x-2 bg-white/10 rounded-full p-1 justify-end">
                    <button
                      type="button"
                      onClick={() => setSuperAdminMode && setSuperAdminMode('student')}
                      className={`px-2 sm:px-3 py-1 rounded-full text-[10px] sm:text-sm ${superAdminMode === 'student' ? 'bg-white/30 text-white' : 'text-white/80 hover:bg-white/20'}`}
                    >
                      Student
                    </button>
                    <button
                      type="button"
                      onClick={() => setSuperAdminMode && setSuperAdminMode('teacher')}
                      className={`px-2 sm:px-3 py-1 rounded-full text-[10px] sm:text-sm ${superAdminMode === 'teacher' ? 'bg-white/30 text-white' : 'text-white/80 hover:bg-white/20'}`}
                    >
                      Teacher
                    </button>
                    <button
                      type="button"
                      onClick={() => setSuperAdminMode && setSuperAdminMode('admin')}
                      className={`px-2 sm:px-3 py-1 rounded-full text-[10px] sm:text-sm ${superAdminMode === 'admin' ? 'bg-white/30 text-white' : 'text-white/80 hover:bg-white/20'}`}
                    >
                      Admin
                    </button>
                  </div>
                  
                  <div className="flex flex-wrap items-center gap-0.5 sm:space-x-2 bg-purple-500/30 rounded-full p-1 justify-end">
                    <span className="hidden sm:inline px-2 text-[10px] font-medium uppercase tracking-[0.1em] text-white/70">Tier:</span>
                    <button
                      type="button"
                      onClick={() => setSuperAdminTier && setSuperAdminTier('standard')}
                      className={`px-2 sm:px-3 py-1 rounded-full text-[10px] sm:text-sm ${superAdminTier === 'standard' ? 'bg-purple-500 text-white' : 'text-white/80 hover:bg-purple-500/50'}`}
                    >
                      <span className="sm:hidden">Std</span>
                      <span className="hidden sm:inline">Standard</span>
                    </button>
                    <button
                      type="button"
                      onClick={() => setSuperAdminTier && setSuperAdminTier('pro')}
                      className={`px-2 sm:px-3 py-1 rounded-full text-[10px] sm:text-sm ${superAdminTier === 'pro' ? 'bg-purple-500 text-white' : 'text-white/80 hover:bg-purple-500/50'}`}
                    >
                      Pro
                    </button>
                  </div>

                  <div className="flex flex-wrap items-center gap-1 sm:gap-2 rounded-full bg-white/10 p-1 hidden sm:flex">
                    <span className="hidden sm:inline px-2 text-xs font-medium uppercase tracking-[0.2em] text-white/70">Palette</span>
                    <button
                      type="button"
                      onClick={() => setBrandPalette && setBrandPalette('dark')}
                      className={`px-2 sm:px-3 py-1 rounded-full text-[10px] sm:text-sm ${brandPalette === 'dark' ? 'bg-white/30 text-white' : 'text-white/80 hover:bg-white/20'}`}
                    >
                      Dark
                    </button>
                    <button
                      type="button"
                      onClick={() => setBrandPalette && setBrandPalette('light')}
                      className={`px-2 sm:px-3 py-1 rounded-full text-[10px] sm:text-sm ${brandPalette === 'light' ? 'bg-white/30 text-white' : 'text-white/80 hover:bg-white/20'}`}
                    >
                      Light
                    </button>
                  </div>
                </div>
              )}

              {currentUser.role === 'student' && (
                <div className="relative">
                  <button onClick={() => setShowNotifications(!showNotifications)} className="p-2 rounded-full hover:bg-white/20 text-white relative" title="Notifications">
                    <Bell className="h-5 w-5" />
                    {unreadCount > 0 && (
                      <span className="absolute -top-1 -right-1 flex min-h-5 min-w-5 items-center justify-center rounded-full bg-red-500 px-1 text-[10px] font-bold text-white ring-2 ring-[#13519C]">
                        {unreadCount > 9 ? '9+' : unreadCount}
                      </span>
                    )}
                  </button>
                  {showNotifications && (
                    <div className="absolute top-full right-0 mt-2 w-96 max-w-[calc(100vw-2rem)] rounded-2xl border border-gray-200 bg-white p-4 shadow-lg z-50">
                      <div className="mb-3 flex items-center justify-between gap-3">
                        <h3 className="font-medium text-gray-900">Notifications</h3>
                        <div className="flex items-center gap-2">
                          {unreadNotificationCount > 0 && (
                            <button
                              type="button"
                              onClick={() => onMarkAllNotificationsRead && onMarkAllNotificationsRead()}
                              className="rounded-full border border-slate-200 px-3 py-1 text-xs font-semibold text-slate-600 transition hover:border-slate-300 hover:bg-slate-50"
                            >
                              Mark all read
                            </button>
                          )}
                          <button
                            onClick={() => setShowNotifications(false)}
                            className="text-gray-400 hover:text-gray-600"
                          >
                            <X className="h-4 w-4" />
                          </button>
                        </div>
                      </div>
                      
                      {studentNotifications.length === 0 && pendingAssignments.length === 0 ? (
                        <p className="text-gray-500 text-center py-4">No new notifications</p>
                      ) : (
                        <div className="space-y-3">
                          {studentNotifications.map((notification) => (
                            <button
                              key={notification.id}
                              type="button"
                              onClick={() => onMarkNotificationRead && onMarkNotificationRead(notification.id)}
                              className={`block w-full rounded-2xl border px-4 py-3 text-left transition ${notification.isRead ? 'border-slate-200 bg-slate-50' : 'border-blue-200 bg-blue-50/80'}`}
                            >
                              <div className="flex items-start justify-between gap-3">
                                <div>
                                  <p className="text-sm font-semibold text-slate-900">{notification.title || 'Notification'}</p>
                                  <p className="mt-1 text-sm leading-6 text-slate-600">{notification.message}</p>
                                </div>
                                {!notification.isRead && <span className="mt-1 h-2.5 w-2.5 shrink-0 rounded-full bg-blue-500" />}
                              </div>
                              <div className="mt-2 flex items-center justify-between text-xs text-slate-500">
                                <span className="uppercase tracking-[0.2em]">{notification.type || 'notice'}</span>
                                <span>{formatNotificationDate(notification.createdAt)}</span>
                              </div>
                            </button>
                          ))}

                          {pendingAssignments.length > 0 && (
                            <div className="rounded-2xl border border-amber-200 bg-amber-50 px-4 py-3 text-sm text-amber-800">
                              Class assignments are not yet available in South Africa.
                            </div>
                          )}
                        </div>
                      )}
                    </div>
                  )}
                </div>
              )}
              <button onClick={() => setShowLogoutConfirm(true)} className="flex items-center space-x-2 bg-white/20 hover:bg-white/30 text-white rounded-full p-2" title="Logout">
                <LogOut className="h-5 w-5" />
              </button>
            </div>
          )}
        </div>
      </div>

      {/* Logout Confirmation Modal */}
      {showLogoutConfirm && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-[100] px-4">
          <div className="bg-white rounded-2xl p-6 max-w-sm w-full shadow-xl">
            <h3 className="text-xl font-bold text-gray-900 mb-2">Confirm Logout</h3>
            <p className="text-gray-600 mb-6">Are you sure you want to log out of your account?</p>
            <div className="flex justify-end space-x-3">
              <button 
                onClick={() => setShowLogoutConfirm(false)}
                className="px-4 py-2 text-gray-700 font-semibold hover:bg-gray-100 rounded-xl transition-colors"
              >
                Cancel
              </button>
              <button 
                onClick={() => {
                  setShowLogoutConfirm(false);
                  if (onLogout) onLogout();
                }}
                className="px-4 py-2 bg-red-600 text-white font-semibold hover:bg-red-700 rounded-xl transition-colors"
              >
                Log Out
              </button>
            </div>
          </div>
        </div>
      )}
    </header>
  );
};

export default Header;
