tcl86t.dll      tk86t.dll       tk              __splash              �  �  �   �   Xtk86t.dll tk\ttk\cursors.tcl tk\ttk\ttk.tcl tk\ttk\utils.tcl tk\tk.tcl tcl86t.dll tk\ttk\fonts.tcl tk\license.terms tk\text.tcl proc _ipc_server {channel clientaddr clientport} {
set client_name [format <%s:%d> $clientaddr $clientport]
chan configure $channel \
-buffering none \
-encoding utf-8 \
-eofchar \x04 \
-translation cr
chan event $channel readable [list _ipc_caller $channel $client_name]
}
proc _ipc_caller {channel client_name} {
chan gets $channel cmd
if {[chan eof $channel]} {
chan close $channel
exit
} elseif {![chan blocked $channel]} {
if {[string match "update_text*" $cmd]} {
global status_text
set first [expr {[string first "(" $cmd] + 1}]
set last [expr {[string last ")" $cmd] - 1}]
set status_text [string range $cmd $first $last]
}
}
}
set server_socket [socket -server _ipc_server -myaddr localhost 0]
set server_port [fconfigure $server_socket -sockname]
set env(_PYIBoot_SPLASH) [lindex $server_port 2]
image create photo splash_image
splash_image put $_image_data
unset _image_data
proc canvas_text_update {canvas tag _var - -} {
upvar $_var var
$canvas itemconfigure $tag -text $var
}
package require Tk
set image_width [image width splash_image]
set image_height [image height splash_image]
set display_width [winfo screenwidth .]
set display_height [winfo screenheight .]
set x_position [expr {int(0.5*($display_width - $image_width))}]
set y_position [expr {int(0.5*($display_height - $image_height))}]
frame .root
canvas .root.canvas \
-width $image_width \
-height $image_height \
-borderwidth 0 \
-highlightthickness 0
.root.canvas create image \
[expr {$image_width / 2}] \
[expr {$image_height / 2}] \
-image splash_image
wm attributes . -transparentcolor magenta
.root.canvas configure -background magenta
pack .root
grid .root.canvas -column 0 -row 0 -columnspan 1 -rowspan 2
wm overrideredirect . 1
wm geometry . +${x_position}+${y_position}
wm attributes . -topmost 1
raise .�PNG

   IHDR   d   d   p�T   	pHYs     ��  �IDATx��	�U�������	P<PT.OJ9D�$۝dw��0Z�����ZA�C��7�-��$ Wq&�ET0RPZH85�d�7G�Iv����03;��=ݻ�W���������w���-hA(��O�����,vKU<C(�X*\,5.�n������i�P���%F󳦕����3�q)��U<���9x.�s���$�Odt�(��[B���?RS9	�^�w�)ӃGN��͌NF��)g����+�!4���e`F�+B��y�2[�
c`$]R��R�o�&'i�����=���?A��{f�R��B�����==�GE7	]�x��7��M*�+5�J�H2)�hzYj�ב_(��D�0���Q%��A����s`�qM�̕�J�/$O J'*z�]�:��D�0^(Z$mO|�:�h�PD��9r��鏉oT�,
��+�#e�ȗ&	EOzsr��P��Q��?$�)9�Q(z�����TLz3R�V��U_�����J��>��ꁡ�.�`������C���.�&nd�P��P�K��|�+��PtlG�>���Y�c�B��fM�q��=���g�3�|}�,Nh\�~"���k������Hxnf���$m��)��Z�i8q���A��Rf ��V�,��5J���5GIM�3m��bZЂ��-hAv��R�@��*n��2W<!��o�0F*:�N���%j�+���ga�h�b�Px�Px��Q;1#'p=�S��נ��nBc)�b'v_9E*t�e�{�E6�<
^ܮK�p@,������״'�շ����dzz?�c�X<&�-5=d�j�ޜ����!Hs]��k�7Y�
����Ϳ�ӈU�D�я����A�0F(�>�M��B�cH�+�!5^����HCE}L;�81���&�Q�rT��]��h����ǰ�}B��]h��m��N@f���8����F�
�k("tdK��O���	CM���~ա���	-5]$_��8�Wh\1�ř2bi�����Ip05a�"�"��N7q��[���o�Ocm�,/�یŵ&A���\�H���@�0ƈ5����-�5���)z�/g��;�8
��w����5��$4���B�����ŏ�,)���R�-R�c���fys�fNE�M���k��p^�ft���j��$�4N��i81�������'zw�m6����7�WKMK�������~�lS��-��x�8�>|��e5C
<0���m�d3���ݥ�8�1<�����2ձ�� ��l�I��wg�H����_ûS�PtR8���B�SR���5��(N��W���V�eF͟,.�N�R>�ܬ_G����]2K�q�6�������&���eC��a���Xv�W4$�޽~Ys��,G��mqNF��Ds	�fʕ�
EgIM?��A�!K��!��a�ɧ���,q���[e�'5����re��$��'�.����֚dn��;f/:����f��Ȩ0'~���b&�9��nX;���>����C�&���pFx�"G-��{���!
��I� 2e�lM:_P��M�2E�,C��]���>pЫ��?Kj<��*� �/���\�/]�l[���SnF'4>ܮ��	��~a��u���5�����=JR�hwDƱ� 0C\��X�\���Kp�����I��2*�/�1�ZفX�[Ӣrf�`��.�&�V�} î���0���F�,�������1u�M�0�=���G���<��]!qe�Wa��~��m(�jǱ�
��pZ���<�;A����и�]SO�m��{���u��U.�K]�z��dH�{�{aB����]6�\C��9q�Ag%�U��^�̚0 ��X�`�]����A2�1��	��R���?s�U��{�n<�-�i��6W�Y�������l��XV[�#j#��9fI���cBӴX�V��\���ö<�8�t�q2�����x,��M�_�X,M��T�'C`����u3
��]�69`i���Z�\^m����<�4B���q���~"Fɐ ��!rP�+�r�9I���f:(3�d��ܻ����8���3�a\f��!^�E؝�W<wɸ�.U���I�?����s�H\�:�f$rB���95�aΧ��c��9�:;2؝JL%z�0pBY�9�s���74{����H�3U\8�1���75�V[���o�2dc?�*�e2#.��]Um/X�G��D쐡�gc�ӏ8ؖ��k}�i`H(K}W�w5R�HR�<˫��-�(ွ�����*AF�L�dC҄וQh�v5�T=�ꄴֻ`_�uhc�ޮ@�M�;����4��I��Q`Ga̸u#_��2C��� V��Ț�㔞n�B�����ymC���AC�1G�x�%�����8Ct�"�gTs�w2���c��1����7
�o$����Q8���"�*g��� J�J��u��xqΒy�k�m4]s����Ñ��꒰t㿭�G֖��e�9J���Q�[�����V��p�Z��M5�[A��pX����6u�!���7���j#]r�k�)]�ojg@���|yFX�;D�1�'V��)�\b�k�2w���'{�*5%�V���`@�<i�F��V�U�r�\�/�ʙ:j��kY@��DT�s����K�"����jd��BS�=7�M�]��xBVG5��M�v���f!����s��}CH�`_�B߾���fnkU��i=?l��Шh�y�c��#��0]��P{�lt^�Ԃkw��5��B6�.A}�e�<�&4R �;a^,C�����o1o����4.�a�*�kP��S:��D~>��"DQB��A�'NW�1>�Ì�,���9 ��:�s��Z12���y����Зj���!�9���6\���k{��* ����	�9`mq��N�*ej3��P��j�X�q���ʮ��'�?��]�S7�ݑ4�um�$�J�_3��/0����x?�Ǖ!�g��U\���#p�g�KEk�&���xsT�o����\��t�"����Oǳ�º���/V�Wl��j!_��>%q� �Ov��5~��}B�EՖ�5?i�W�+"	bq�$�p���t��5ժ�8ف�EI3a��z+tnV5�~���NjM���xgB��tTͲl�wŹ[�ei/�=I����|���5�0�bħc14X�q�����iӸ\�憱�#b���%���KƵ��^;��L#S(:����ʹ`on2C��cF��dAf�<�?�q���At��M�j���/:`��Flv�>F�Z��<�ŝwr�9���^��y�����-�����c��}�t��ʭw���7��>���F,�Z��h���� .t킽<»�Y6��ڀf4B�'Ʈv�q����5���#�pĸ��u���}X�4�iB�}��`f�s\V��%�g�CO��I�Ŝk3J�    IEND�B`�